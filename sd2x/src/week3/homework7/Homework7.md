# Homework 7 - UML

In this assignment you will implement a design that is specified using a UML class diagram.

In completing this assignment, you will:

- Gain more experience understanding how a class design is represented in UML
- Apply what you have learned about converting a UML class diagram to Java code

## Debugging/Error Note

If you run into errors/bugs/don't understand the output that Codio is giving you, please post in the Discussion Forum and a TA will assist you! Please do NOT email Codio as they will not review any errors you are getting.

## Background

The UML class diagram below represents a game involving mazes that consist of rooms:

![UML](https://studio.edx.org/asset-v1:PennX+SD2x+2T2017+type@asset+block@hw7_uml.jpg)

## Activity

Implement the design in Java by creating classes according to the class diagram and following these guidelines:

- You do not have to actually implement the methods and game logic, of course, but your code must compile: you can have methods return null as needed.
- You do not need to worry about any sort of main method or other classes/methods; just represent the classes as shown above.
- All fields and methods should be `public` (that’s what the little plus-sign next to the method names indicates). You do not need to worry about getters and setters.
- All classes and interfaces must be `public`.
- All concrete classes should have a no-argument constructor.
- Use arrays to implement multiplicity, e.g. if class Person has a “zero or more” relationship with class Pet, represent it as a Pet[ ] field in Person (as opposed to, say, a List< Pet > or Set< Pet >)
- MapSite should be an abstract class with a concrete “enter” method that does nothing.
- All classes must be in the default package, i.e. there should be no “package” declaration at the top of the source code.

## Helpful Hints

Think about how the different UML relationships are reflected in the implementation, and keep in mind that not all relationships imply that one class “is” or “has” another as a superclass or field.

Also pay close attention to how multiplicity is represented in the UML and think about what that means for the types of the fields.

If you're having trouble remembering the meaning of the different arrows, you can of course review the lesson, or look at this detailed reference guide: [UML Class Diagrams: Reference](https://msdn.microsoft.com/en-us/library/dd409437.aspx)

## Before You Submit

Please be sure that:

- all classes are in the default package, i.e. there is no “package” declaration at the top of the source code
- your classes compile

## Assessment

Your submission will be assessed using automatic grading scripts that will check that your implementation matches the specified design, specifically that each class:

- extends the correct parent class and/or implements the correct interfaces
- is abstract or concrete as specified
- has the correct number of fields and methods
- has fields of the correct name, type, and multiplicity
- has methods of the correct name, parameter type(s), and return type

Your score is determined by the percentage of these tests that “pass,” i.e. that correctly implement the various aspects of the design.

Before submitting your solution, you can run these grading scripts locally on your computer by following the steps below. These instructions assume you are using Eclipse, but should be applicable to other IDEs as well:

1. Download the JUnit distribution at [junit-dist.jar](https://courses.edx.org/assets/courseware/v1/2ed6e73287692ad54165a95ba8e5ac11/asset-v1:PennX+SD2x+2T2019+type@asset+block/junit-dist.jar) and save it in your project's root directory. You should be able to do this by dragging it from Finder/Explorer into Eclipse and dropping it in the folder that has the same name as your project. Then add it to the project's build path by right-clicking the file name in Eclipse to get the pop-up/context menu, then selecting "Build Path -->" and then "Add to Build Path."
2. Download the tests at [homework7-tests.jar](https://courses.edx.org/assets/courseware/v1/1688dfe80723c6be33d91e8a56bef157/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework7-tests.jar), and add it to the Eclipse project's build path as above.
3. Now run the tests by right-clicking homework7-tests.jar in Eclipse to get the pop-up/context menu and selecting "Run As -->" and then "Java Application." You should see the tests run in the console and it should tell you your score for this assignment, or "Great job!" if your score would be 100%.

Alternatively, if you would like to run the autograder from the command line, put the two .jar files and your .class files for this assignment in the same directory along with the .txt files that you downloaded, and run:

**Mac/Linux:** java -cp .:junit-dist.jar:homework7-tests.jar Homework7Grader

**Windows:** java -cp .;junit-dist.jar;homework7-tests.jar Homework7Grader

This will add junit-dist.jar and homework7-tests.jar to the classpath and then run Java with Homework7Grader as the main class.
