import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    total_pages = len(corpus)
    # probability for a page with no links
    prob = 0
    prob_random = 1 / total_pages

    # probability for a page containing links
    if len(corpus[page]) > 0:
        prob = damping_factor / len(corpus[page])
        prob_random = (1 - damping_factor) / total_pages

    # Populating result with probabilities
    result = {}
    for pag in corpus:
        result[pag] = prob_random
    for pag in corpus[page]:
        result[pag] += prob

    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    result = {}
    # initialising result dict for frequncy count
    for page in corpus:
        result[page] = 0

    # choose first value randomly
    page = random.choice(list(corpus.keys()))
    result[page] += 1

    # choose additional values from previous value
    for i in range(n-1):
        model = transition_model(corpus, page, damping_factor)
        page = random.choices(
            population=list(model.keys()),
            weights=list(model.values()),
            k=1
        )[0]
        result[page] += 1

    # calculate final pageranks
    for page in result:
        result[page] /= n

    return result


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    total_pages = len(corpus)

    # initialize pageranks with initial value
    pagerank = {}
    links = {}
    initial_value = 1.0 / total_pages
    for page in corpus:
        pagerank[page] = initial_value
        links[page] = set()

    # create reverse link dict
    for page, link in corpus.items():
        if len(link) == 0:
            # If page has no links then add it to all pages
            for l in corpus:
                links[l].add(page)
            continue
        for l in link:
            links[l].add(page)

    prob_random = (1.0 - damping_factor) / total_pages

    while True:
        # calculate new pagerank
        new_pagerank = {}
        for page in pagerank:
            sum = 0.0
            for link in links[page]:
                # if link has no outgoing links then divide by number of total pages
                if len(corpus[link]) == 0:
                    sum += pagerank[link] / total_pages
                else:
                    sum += pagerank[link] / len(corpus[link])
            new_pagerank[page] = prob_random + damping_factor * sum

        # check difference threshold
        if max_dif(pagerank, new_pagerank) < 0.001:
            break

        pagerank = new_pagerank

    return pagerank


def max_dif(a, b):
    """
    Returns the maximum distance between each value of a and b.
    """
    maximum = 0.0
    for page in a:
        maximum = max(maximum, abs(a[page] - b[page]))

    return maximum


if __name__ == "__main__":
    main()
