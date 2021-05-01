import nltk
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    from os import scandir

    # get all .txt files and their paths
    file_list = [
        (f.name, f.path)
        for f in scandir(directory)
        if f.is_file() and f.name.endswith('.txt')
    ]

    # read file contents
    result = {}
    for name, path in file_list:
        result[name] = ''.join(open(path).readlines())

    return result


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    import string

    # pre-defined punctuations and stopwords
    filter_out = [char for char in string.punctuation]
    filter_out.extend(nltk.corpus.stopwords.words('english'))

    tokens = nltk.word_tokenize(document)

    # remove invalid tokens
    words = [
        word.lower()
        for word in tokens
        if word.lower() not in filter_out
    ]

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    from math import log

    total = len(documents)
    word_set = set(
        word
        for content in documents.values()
        for word in content
    )

    word_idfs = {}
    for word in word_set:
        # number of documents word appears in
        num = 0
        for content in documents.values():
            if word in content:
                num += 1

        # calculate idf value
        word_idfs[word] = log(total / num)

    return word_idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    scores = []
    for filename, content in files.items():
        sum = 0
        for word in query:
            # number of times the word appears
            num = content.count(word)
            if num == 0:
                continue

            # calculate tf-idf value if word exists in file
            sum += num * idfs[word]
        scores.append((filename, sum))

    # reverse sort by tf-idf values and get first n names
    scores.sort(key=lambda x: x[1], reverse=True)
    top_filenames = [x[0] for x in scores[:n]]

    return top_filenames


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    scores = []
    for sentence, sen_words in sentences.items():
        sum, num_words = 0, 0
        for word in query:
            # number of times word appears in sentence
            num = sen_words.count(word)
            if num == 0:
                continue

            sum += idfs[word]
            num_words += num

        # calculate term density
        term_density = num_words / len(sen_words)
        scores.append((sentence, sum, term_density))

    # reverse sort by first idf, then term_density values and get first n sentences
    scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    top_sen = [x[0] for x in scores[:n]]

    return top_sen


if __name__ == "__main__":
    main()
