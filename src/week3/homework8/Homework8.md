# Homework 8 - Software Design

In this assignment, you are asked to implement a program that allows a user to search through a collection of books and find books written by a specific author or the number of books written in a specified year. You will implement this program using the three-tier architecture discussed in recent lessons.

In completing this assignment, you will:

- Apply what you have learned about software architecture, software design, and internal quality
- Consider the tradeoffs of software design, especially the input and output of methods, as it relates to software quality

## Debugging/Error Note

If you run into errors/bugs/don't understand the output that Codio is giving you, please post in the Discussion Forum and a TA will assist you! Please do NOT email Codio as they will not review any errors you are getting.

## Getting Started

Download the following files:

- [PresentationTier.java](https://courses.edx.org/assets/courseware/v1/b3bdb95be609f5c1678d8363b2b3c4c3/asset-v1:PennX+SD2x+2T2019+type@asset+block/PresentationTier.java): the class that represents the “presentation tier,” which handles interaction with the user
- [LogicTier.java](https://courses.edx.org/assets/courseware/v1/b25a2e36fd2515dc9f55ad4f5e13c42b/asset-v1:PennX+SD2x+2T2019+type@asset+block/LogicTier.java): the class that represents the “logic tier,” which includes processing and performing computations on data
- [DataTier.java](https://courses.edx.org/assets/courseware/v1/48b3ae1488d657452b72c391aed4e1b4/asset-v1:PennX+SD2x+2T2019+type@asset+block/DataTier.java): the class that represents the “data tier,” which handles reading data from some source and making it available to the rest of the program
- [Book.java](https://courses.edx.org/assets/courseware/v1/6b20ddfb2f185b8cf7853ccd2eaa8136/asset-v1:PennX+SD2x+2T2019+type@asset+block/Book.java): represents a single book in our program
- [Main.java](https://courses.edx.org/assets/courseware/v1/9a318177978962d3fbf9e4e6e2ad0b94/asset-v1:PennX+SD2x+2T2019+type@asset+block/Main.java): responsible for instantiating the objects and setting up their relations

Also download [books.txt](https://courses.edx.org/assets/courseware/v1/3571071f5880d95a9e4dc8fb2263cd25/asset-v1:PennX+SD2x+2T2019+type@asset+block/books.txt), which contains a list of popular books in tab-separated format. Each row represents one book and has the following format:

`[title][tab][author][tab][year]`

You may use your own list of books for testing your application as you implement it, but the correctness of your solution will be determined using the file we provide.

## Activity

This program is perhaps not difficult to implement but the challenge here is applying good software design principles (modularity, functional independence, and abstraction) in order to create code that has high internal quality: changeability, stability, understandability, and testability.

In particular, you need to apply the three-tier architecture, which we will simplify by saying that each tier only has one class. Your goal is to put the right functionality into the right tiers/classes, decide on method inputs and outputs, and then implement the code.

In practice, there may be some flexibility as to whether certain functionality goes into a single method or multiple methods, what the names of the methods would be, etc. And you generally would have multiple classes per tier, and not just a single class.

In order to simplify the automatic grading of this assignment, in this case the application you implement must have the following methods:

- **findBookTitlesByAuthor:** for a given name, search through all of the books and return the titles of those books whose author name includes the input name.
- **findNumberOfBooksInYear:** for a given year, search through all of the books and return the number of books published in that year
- **getAllBooks:** read the data file containing information about the books, create Book objects for each, and then return the Book objects.
- **showBookTitlesByAuthor:** using the command-line (i.e., reading from System.in), ask the user to enter part or all of an author’s name, then display (using System.out) the titles of those books whose author name includes the input name.
- **showNumberOfBooksInYear:** using the command-line (i.e., reading from System.in), ask the user to enter a year, then display (using System.out) the number of books published in that year

Both _findBookTitlesByAuthor_ and _showBookTitlesByAuthor_ should look for partial matches and should ignore case, i.e. be case-insensitive. The titles of the books that are returned/displayed should be sorted based on the year they were published in non-descending order; if two or more books have the same publication year, those books should be sorted alphabetically.

For each of the five methods, you need to decide:

- In which class (_PresentationTier_, _LogicTier_, or _DataTier_) should it be implemented?
- What should its input parameter(s) be?
- What should its return type be?

In addition to considering modularity and functional independence in applying the three-tier architecture, be sure to also consider abstraction when designing each method: the caller of a method should be able to use it knowing only what it does, and not the details of how it works.

Once you have completed your design, implement each of the five methods according to the specifications above.

In all cases, you can handle error conditions in any way you choose, e.g. if the user enters a year that is non-numeric in _showBookTitlesByAuthor_, if the name specified in _findBookTitlesByAuthor_ is null, etc. Just be sure your code works correctly for “normal” inputs.

Likewise, it is okay for getAllBooks to assume that the input file exists and is well-formatted.

You can use any prompt you choose for asking for input in _showBookTitlesByAuthor_ and _showNumberOfBooksInYear_, and can likewise choose any output formatting you like.

Finally, implement _PresentationTier.start_ so that it asks the user which feature they would like to use and invokes the appropriate methods in the appropriate classes. Once the output has been displayed, the program should terminate. As above, you can handle error cases in any way that you deem appropriate.

Please be sure that your code adheres to the following guidelines and restrictions:

- Each method listed above must go into exactly one of the three classes (PresentationTier, LogicTier, or DataTier).
- Do not add any other classes, though you may add additional fields and methods as necessary.
- Do not change the Book class or Main class.
- All methods must be public.
- All code should be in the default package, i.e. there should be no “package” declaration at the top of the source code.

## Helpful Hints

As you have probably already noticed, the examples discussed in the lessons are very similar to this program. Use those as guidelines and consider where the functionality went in those examples, and what inputs/outputs each method had.

The getAllBooks method needs to read from the input file. If you do not have prior experience writing Java code to read a text file, feel free to look online for help. There is good documentation at: [docs.oracle](https://docs.oracle.com/javase/tutorial/essential/io/file.html) and good tutorials elsewhere online.

## Before You Submit

Please be sure that:

- your _PresentationTier_, _LogicTier_, and _DataTier_ classes are in the default package, i.e. there is no “package” declaration at the top of the source code
- your _PresentationTier_, _LogicTier_, and _DataTier_ classes compile and you have not changed the names of any of the five methods listed above
- you have not created any additional .java files
- you have not made any changes to Book.java or Main.java (you do not need to submit these files) and both still compile

## Assessment

Your submission will be assessed using automatic grading scripts that will check the following criteria:

- Are methods implemented in the correct classes, i.e. do you correctly apply the three-tier architecture.
- Do the methods have the correct input parameters and return type, i.e. do you correctly apply functional independence and abstraction
- Do the methods work correctly according to the specification?

Your score is determined by the percentage of these tests that “pass,” i.e. that demonstrate that you have designed the program correctly and that produce the correct result for the specified input.

Before submitting your solution, you can run these grading scripts locally on your computer by following the steps below. These instructions assume you are using Eclipse, but should be applicable to other IDEs as well:

1. Download the JUnit distribution at [junit-dist.jar](https://courses.edx.org/assets/courseware/v1/2ed6e73287692ad54165a95ba8e5ac11/asset-v1:PennX+SD2x+2T2019+type@asset+block/junit-dist.jar) and save it in your project's root directory. You should be able to do this by dragging it from Finder/Explorer into Eclipse and dropping it in the folder that has the same name as your project. Then add it to the project's build path by right-clicking the file name in Eclipse to get the pop-up/context menu, then selecting "Build Path -->" and then "Add to Build Path."
2. Download the tests at [homework8-tests.jar](https://courses.edx.org/assets/courseware/v1/1688dfe80723c6be33d91e8a56bef157/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework8-tests.jar), and add it to the Eclipse project's build path as above.
3. Also download the test input files from [homework8-files.zip](https://courses.edx.org/assets/courseware/v1/f1f6a2aa80aae9d3bbe9696f9e3810d7/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework8-files.zip). Unzip this file on your computer and copy the two .txt files into your Eclipse project; you should be able to drag and drop them right into Eclipse. Make sure you put them in your project's root directory, as you did with the two .jar files.
4. Now run the tests by right-clicking homework8-tests.jar in Eclipse to get the pop-up/context menu and selecting "Run As -->" and then "Java Application." You should see the tests run in the console and it should tell you your score for this assignment, or "Great job!" if your score would be 100%.

Alternatively, if you would like to run the autograder from the command line, put the two .jar files and your .class files for this assignment in the same directory along with the .txt files that you downloaded, and run:

**Mac/Linux:** java -cp .:junit-dist.jar:homework8-tests.jar Homework8Grader

**Windows:** java -cp .;junit-dist.jar;homework8-tests.jar Homework8Grader

This will add junit-dist.jar and homework8-tests.jar to the classpath and then run Java with Homework8Grader as the main class.
