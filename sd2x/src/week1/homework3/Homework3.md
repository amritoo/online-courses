# Homework 3 - Collections

In this assignment, you will write a program that will analyze the sentiment (positive or negative) of a sentence based on the words it contains by implementing methods that use the List, Set, and Map interfaces from the Java Collections API.

In completing this assignment, you will:

- Become familiar with the methods in the java.util.List, java.util.Set, and java.util.Map interfaces
- Continue working with abstract data types by using only the interface of an implementation
- Apply what you have learned about how lists, sets, and maps work
- Get a better understanding of the difference between lists and sets
- Demonstrate that you can use lists, sets, and maps to solve real-world problems
- Gain experience writing Java code that reads an input file

## Debugging/Error Note

If you run into errors/bugs/don't understand the output that Codio is giving you, please post in the Discussion Forum and a TA will assist you! Please do NOT email Codio as they will not review any errors you are getting.

## Background

Sentiment analysis is a task from the field of computational linguistics that seeks to determine the general attitude of a given piece of text. For instance, we would like to have a program that could look at the text “This assignment was joyful and a pleasure” and realize that it was a positive statement while “It made me want to pull out my hair” is negative.

One algorithm that we can use for this is to assign a numeric value to any given word based on how positive or negative that word is and then determine the overall sentiment of the statement based on the average values of the words.

To determine the sentiment of an individual word, we can use a corpus of statements, each of which has **an overall score already assigned to it**. The sentiment of an individual word equals the **average** of the statements in which that word appears.

For instance, our corpus may look like this:

```text
0 This was not as much fun as I thought it would be .

1 I had a lot of fun on this and learned a lot .

-1 It would be more fun if we had more time to work on it .

2 I didn’t think programming in Java could be so much fun !

-2 I would have preferred an easier assignment .

2 I can’t think of anything more fun than learning Java !
```

Each statement is labeled with a score from -2 to 2 as follows:

-2: very negative

-1: somewhat negative

0: neutral

1: somewhat positive

2: very positive

To determine the overall sentiment of the word “fun,” we take the average of the sentences in which it appears. In this case, it would be (0 + 1 + -1 + 2 + 2) / 5 = 0.8.

Then, given a new sentence, we can determine its sentiment by computing the average of the sentiments of the individual words it contains. The sentiment of any previously unseen word would be 0.

Your program will be evaluated using a set of ~8,500 movie reviews that have been provided to you in the file [reviews.txt](https://courses.edx.org/assets/courseware/v1/d713dacc081c1e7e9a7199d61d1d2790/asset-v1:PennX+SD2x+2T2019+type@asset+block/reviews.txt). You can, of course, create your own input file for testing, but the correctness of your program will be determined using this file.

## Getting Started

Download [Sentence.java](https://courses.edx.org/assets/courseware/v1/1624e91d25ec94a91eadd94bb8dbea79/asset-v1:PennX+SD2x+2T2019+type@asset+block/Sentence.java) and [Word.java](https://courses.edx.org/assets/courseware/v1/0c81b0cd60dbd1d28f993292a7ad31f0/asset-v1:PennX+SD2x+2T2019+type@asset+block/Word.java), which represent a single sentence from the input file and a distinct word in the file, respectively.

Last, download [Analyzer.java](https://courses.edx.org/assets/courseware/v1/10dbee7c7eeb5621aaf28cf77551f0f4/asset-v1:PennX+SD2x+2T2019+type@asset+block/Analyzer.java), which contains the “main” method for the program, as well as the unimplemented methods for the code that you will write in this assignment.

## Activity

### Part 1. Reading the corpus as an input file

Implement the `readFile` method in **Analyzer.java**.

This method should take the name of the file to read and read it one line at a time, creating Sentence objects and putting them into the List. Note that the method returns a List containing Sentence objects.

For a valid sentence such as:

2 I am learning a lot .”

then the `score` field of the Sentence object should be set to 2, and the `text` field should be “I am learning a lot .”

Your code should ignore (and not create a Sentence object for) any line that is not well-formatted, which we assume to mean “starts with an int between -2 and 2 (inclusive), has a single whitespace, and then is followed by more text.”

However, if the file cannot be opened for reading or if the input filename is null, this method should return an empty List.

Note that it is up to you to determine which List implementation to return; any decision is fine, as long as it implements the List interface and you do not change the signature of this method.

If you do not have prior experience writing Java code to read a text file, feel free to look online for help. There is good documentation at [file](https://docs.oracle.com/javase/tutorial/essential/io/file.html) and good tutorials elsewhere online.

Please do not change the signature of the _readFile_ method and do not modify _Sentence.java_. Also, please do not create new .java files. If you need to create new classes, add them to _Analyzer.java_. Last, please make sure that your _Analyzer_ class is in the default package, i.e. there is no “package” declaration at the top of the source code.

### Part 2. Calculating the sentiment of each word

Implement the `allWords` method in Analyzer.java (the same file as Part 1).

This method should find all of the individual tokens/words in the text field of each Sentence in the List and create Word objects for each distinct word. The Word objects should keep track of the number of occurrences of that word in all Sentences, and the total **cumulative** score of all Sentences in which it appears. This method should then return a Set of those Word objects.

If the input List of Sentences is null or is empty, the allWords method should return an empty Set.

If a Sentence object in the input List is null, this method should ignore it and process the non-null Sentences.

As you can see, `allWords` needs to tokenize/split the text of each Sentence to get the individual words. Consult the Java documentation for help with this:

- [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)
- [StringTokenizer](https://docs.oracle.com/javase/8/docs/api/java/util/StringTokenizer.html)

or feel free to find a tutorial online.

Keep in mind that when you tokenize the text of each Sentence, you will be getting Strings, but the Set that this method returns needs to include Word objects. However, if two Strings are equal, they should be combined into the same Word object, which should track the cumulative score of all Sentences containing that String.

As you may have noticed in the data file we provided, some tokens start with punctuation and the first word of each sentence starts with a capital letter. In producing the Set of Words, **your program should ignore any token that does not start with a letter**. Also, this method should convert all strings to **lowercase** so that it is case-insensitive. Do not assume that the strings in the Sentence objects have already been converted to lowercase.

As an example, consider this text:

`It 's a lot of fun to learn about data structures.`

Your program should convert " `It` " to " `it` " (to make it lowercase) and ignore " `'s` " and the period at the end of the sentence since those tokens do not start with a letter.

As in Part 1, it is up to you to determine which Set implementation to return; any decision is fine, as long as it implements the Set interface and you do not change the signature of this method.

Hint: although this method needs to return a Set of Words, you may find it easier to use a different data structure while processing each Sentence, and then put the combined results into a Set before the method returns. There is not necessarily a single "correct" way to implement this method, as long as you return the proper Set of Words at the end.

Please do not change the signature of the _allWords_ method and do not modify _Sentence.java_ or _Word.java_. Also, please do not create new .java files. If you need to create new classes, add them to _Analyzer.java_. Last, please make sure that your _Analyzer_ class is in the default package, i.e. there is no “package” declaration at the top of the source code.

### Part 3. Storing the sentiment of each word

Implement the `calculateScores` method in Analyzer.java (the same file as Parts 1 and 2).

This method should iterate over each Word in the input Set, use the Word’s `calculateScore` method to get the average sentiment score for that Word, and then place the text of the Word (as key) and calculated score (as value) in a Map.

If the input Set of Words is null or is empty, the calculateScores method should return an empty Map.

If a Word object in the input Set is null, this method should ignore it and process the non-null Words.

As above, it is up to you to determine which Map implementation to return; any decision is fine, as long as it implements the Map interface and you do not change the signature of this method.

Please do not change the signature of the _calculateScores_ method and do not modify _Sentence.java_ or _Word.java_. Also, please do not create new .java files. If you need to create new classes, add them to _Analyzer.java_. _Analyzer_ class is in the default package, i.e. there is no “package” declaration at the top of the source code.

### Part 4. Determining the sentiment of a sentence

Finally, implement the `calculateSentenceScore` method in Analyzer.java.

This method should use the Map to calculate and return the average score of all the words in the input sentence.

Note that you will need to tokenize/split the sentence, as you did in Part 2.

If a word in the sentence does not start with a letter, then you can ignore it, but if it starts with a letter and is not present in the Map, assign it a score of 0.

You may assume that all words in the Map consist only of lowercase letters (since this would have been done in previous steps) but do not assume that all words in the input sentence consist only of lowercase letters; you should convert them to lowercase before checking whether they’re contained in the Map.

If the input Map is null or empty, or if the input sentence is null or empty or does not contain any valid words, this method should return 0.

Although you can (should!) test each method individually, you can test the entire program using the main method in Analyzer.java. Be sure to specify the name of the input file as the argument to main.

Please do not change the signature of the _calculateSentenceScore_ method and do not modify _Sentence.java_ or _Word.java_. Also, please do not create new .java files. If you need to create new classes, add them to _Analyzer.java_. Last, please make sure that your _Analyzer_ class is in the default package, i.e. there is no “package” declaration at the top of the source code.

## Helpful Hints

Documentation about the methods in the List, Set, and Map interfaces are available as part of the Java API docs:

- [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)
- [Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)
- [Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)

Refer to this documentation if you need help understanding the methods that are available to you.

In implementing this program, we recommend that you implement and test each of the four methods one at a time. That is, rather than implementing all four methods and then hoping it all works correctly, do Part 1 and convince yourself that it works, then do Part 2 (either using the output of Part 1, or input that you create by hand) and convince yourself that it works, and so on. It’s a lot easier to debug this way!

## Before You Submit

Please be sure that:

- your Analyzer class is in the default package, i.e. there is no “package” declaration at the top of the source code
- your Analyzer class compiles and you have not changed the signatures of any of the four methods you implemented
- you have not created any additional .java files and have not made any changes to Sentence.java or Word.java (you do not need to submit these files)

## Assessment

Your submission will be assessed using automatic grading scripts that will check that the methods work correctly for various inputs. Your score is determined by the percentage of these tests that “pass,” i.e. that produce the correct result for the specified input.

For each method, be sure that your implementation covers everything described in the specification, including error handling, and that you consider different categories or classes of inputs, e.g. words that are uppercase/lowercase, words that are not in the Map, words that appear exactly once as opposed to many times, etc.

Before submitting your solution, you can run these grading scripts locally on your computer by following the steps below. These instructions assume you are using Eclipse, but should be applicable to other IDEs as well:

1. Download the JUnit distribution at [junit-dist.jar](https://courses.edx.org/assets/courseware/v1/2ed6e73287692ad54165a95ba8e5ac11/asset-v1:PennX+SD2x+2T2019+type@asset+block/junit-dist.jar) and save it in your project's root directory. You should be able to do this by dragging it from Finder/Explorer into Eclipse and dropping it in the folder that has the same name as your project. Then add it to the project's build path by right-clicking the file name in Eclipse to get the pop-up/context menu, then selecting "Build Path -->" and then "Add to Build Path."
2. Download the tests at [homework3-tests.jar](https://courses.edx.org/assets/courseware/v1/1688dfe80723c6be33d91e8a56bef157/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework3-tests.jar), and add it to the Eclipse project's build path as above.
3. Also download the test input files from [homework3-files.zip](https://courses.edx.org/assets/courseware/v1/ce2d344054dcb53a3a3889a8af11a333/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework3-files.zip). Unzip this file on your computer and copy the seven .html files into your Eclipse project; you should be able to drag and drop them right into Eclipse. Make sure you put them in your project's root directory, as you did with the two .jar files.
4. Now run the tests by right-clicking homework3-tests.jar in Eclipse to get the pop-up/context menu and selecting "Run As -->" and then "Java Application." You should see the tests run in the console and it should tell you your score for this assignment, or "Great job!" if your score would be 100%.

Alternatively, if you would like to run the autograder from the command line, put the two .jar files and your .class files for this assignment in the same directory along with the .html files that you downloaded, and run:

**Mac/Linux:** java -cp .:junit-dist.jar:homework3-tests.jar Homework3Grader

**Windows:** java -cp .;junit-dist.jar;homework3-tests.jar Homework3Grader

This will add junit-dist.jar and homework3-tests.jar to the classpath and then run Java with Homework3Grader as the main class.
