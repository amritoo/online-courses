# Homework 1 - Linked Lists

In this assignment you will implement three methods that perform functions on a linked list, using the java.util.LinkedList class from the Java Collections API.

In completing this assignment, you will:

- Become familiar with the methods in the java.util.LinkedList class
- Apply what you have learned about how linked lists store data
- Demonstrate that you can use linked lists to solve data-related problems

## Getting Started

Download the [LinkedListUtils.java](https://courses.edx.org/assets/courseware/v1/276899496d83bbfb170d072d6eb754be/asset-v1:PennX+SD2x+2T2019+type@asset+block/LinkedListUtils.java) file, which contains the unimplemented methods for the code that you will write in this assignment.

## Debugging/Error Note

If you run into errors/bugs/don't understand the output that Codio is giving you, please post in the Discussion Forum and a TA will assist you! Please do NOT email Codio as they will not review any errors you are getting.

## Activity

Implement the following methods in the **LinkedListUtils.java** file:

**insertSorted:** This method assumes the input LinkedList is already sorted in non-descending order (i.e.,such that each element is greater than or equal to the one that is before it, and inserts the input `int` value into the correct location of the list. Note that the method does not return anything, but rather modifies the input LinkedList as a side effect. If the input LinkedList is null, this method should simply terminate.

**removeMaximumValues:** This method removes all instances of the N largest `values` in the LinkedList. Because the values are Strings, you will need to use the String class’ `compareTo` method to find the largest elements; see the Java API for help with that method. If the input LinkedList is null or if N is non-positive, this method should simply return without any modifications to the input LinkedList. Keep in mind that if any of the N largest values appear more than once in the LinkedList, this method should return remove all instances, so it may remove more than N elements overall. The other elements in the LinkedList should not be modified and their order must not be changed.

**containsSubsequence:** This method determines whether any part of the first LinkedList contains all elements of the second in the same order with no other elements in the sequence, i.e. it should return true if the second LinkedList is a subsequence of the first, and false if it is not. The method should return false if either input is null or empty.

Please do not change the signatures of these three methods (their parameter lists, names, and return value types) and do not create any additional .java files for your solution. If you need additional classes, you can define them in LinkedListUtils.java. Additionally, please be sure that your LinkedListUtils class is in the default package, i.e. there is no “package” declaration at the top of the source code.

## Helpful Hints

Documentation about the methods in the LinkedList class in the latest version of Java is available at [LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html). Refer to this documentation for more direction on using the methods that are available to you.

Keep in mind that the methods in the LinkedList class handle things like updating the nodes’ “next” reference, checking that the head/tail is not null, etc. Although you do not have access to the nodes, this should help simplify much of what you need to do; all you need to focus on is using the LinkedList methods.

## Before You Submit

Please be sure that:

- your LinkedListUtils class is in the default package, i.e. there is no “package” declaration at the top of the source code
- your LinkedListUtils class compiles and you have not changed the signature of the insertSorted, removeMaximumValues, or containsSubsequence methods
- you have not created any additional .java files

## Assessment

Your submission will be assessed using automatic grading scripts that will check that the methods work correctly for various inputs. Your score is determined by the percentage of these tests that “pass,” i.e. that produce the correct result for the specified input. See how to run the automatic grader [here](https://www.youtube.com/watch?v=nRfKqbRGh6A).

For each method, be sure that your implementation covers everything described in the specification, including error handling, and that you consider different categories or classes of inputs, e.g. a particular value being at the front of the LinkedList, the middle of the LinkedList, the rear of the LinkedList, etc.

Before submitting your solution, you can run these grading scripts locally on your computer by following the steps below. These instructions assume you are using Eclipse, but should be applicable to other IDEs as well:

1. Download the JUnit distribution at [junit-dist.jar](https://courses.edx.org/assets/courseware/v1/2ed6e73287692ad54165a95ba8e5ac11/asset-v1:PennX+SD2x+2T2019+type@asset+block/junit-dist.jar) and save it in your project's root directory. You should be able to do this by dragging it from Finder/Explorer into Eclipse and dropping it in the folder that has the same name as your project. Then add it to the project's build path by right-clicking the file name in Eclipse to get the pop-up/context menu, then selecting "Build Path -->" and then "Add to Build Path."
2. Download the tests at [homework1-tests.jar](https://courses.edx.org/assets/courseware/v1/4d42e8c8b68c3ea62e80da2374dc8739/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework1-tests.jar), and add it to the Eclipse project's build path as above.
3. Now run the tests by right-clicking homework1-tests.jar in Eclipse to get the pop-up/context menu and selecting "Run As -->" and then "Java Application." You should see the tests run in the console and it should tell you your score for this assignment, or "Great job!" if your score would be 100%.

Alternatively, if you would like to run the autograder from the command line, put the two .jar files and your .class file for this assignment in the same directory and run the following command:

**Mac/Linux:** java -cp .:junit-dist.jar:homework1-tests.jar Homework1Grader

**Windows:** java -cp .;junit-dist.jar;homework1-tests.jar Homework1Grader

This will add _junit-dist.jar_ and _homework1-tests.jar_ to the classpath and then run Java with _Homework1Grader_ as the main class.
