# Homework 6 - Graphs

In this assignment, you will implement methods used for exploring graphs.

In completing this assignment, you will:

- Become more familiar with the “adjacency set” representation of a graph
- Apply what you have learned about how to traverse a graph
- Demonstrate that you can use graphs to solve common problems in Computer Science

## Debugging/Error Note

If you run into errors/bugs/don't understand the output that Codio is giving you, please post in the Discussion Forum and a TA will assist you! Please do NOT email Codio as they will not review any errors you are getting.

## Getting Started

Begin by downloading the [starter code in this zip file](https://courses.edx.org/assets/courseware/v1/114ac7e923b2aa4cf9adf43cae18eb3b/asset-v1:PennX+SD2x+2T2019+type@asset+block/Graph-code.zip).

This zip file includes the following **.java** files: **Graph**, **UndirectedGraph**, **DirectedGraph**, **Edge**, **Node**, **BreadthFirstSearch**, and **DepthFirstSearch**. These files include the implementations for the adjacency set representation of a graph (undirected and directed) along with breadth-first search and depth-first search implementations that we saw in the lessons.

We have also provided **GraphBuilder.java**, which includes static methods for generating directed and undirected graphs from an input file. These methods assume that the input file is formatted as follows:

- each line of the file consists of the values/labels of two nodes in the graph, separated by a single whitespace
- there is an edge in the graph between the two nodes; if the graph is directed, the edge is directed from the first node to the second

For instance, if the input file looked like this:

```text
cat dog
dog platypus
```

and the graph were directed, there would be an edge from “cat” to “dog,” and from “dog” to “platypus.”

We have provided a file **graph_builder_test.txt** that you can use as input for testing the methods that you will implement in this assignment. You are, of course, free to create your own input files, but this is the file we will use to assess your solution. If you are using Eclipse, be sure to put this file in the root directory of your project.

Last, **GraphUtils.java** contains the unimplemented methods for the code that you will write in this assignment.

## Activity

Implement the following methods in the **GraphUtils.java** file:

**minDistance:** Given a Graph, this method returns the shortest distance (in terms of number of edges) from the node labeled src to the node labeled dest. The method should return -1 for any invalid inputs, including: null values for the Graph, src, or dest; there is no node labeled src or dest in the graph; there is no path from src to dest. Keep in mind that this method does not just return the distance of **any** path from src to dest, it must be the **shortest** path.

**nodesWithinDistance:** Given a Graph, this method returns a Set of the values of all nodes within the specified distance (in terms of number of edges) of the node labeled src, i.e. for which the minimum number of edges from src to that node is less than or equal to the specified distance. The value of the node itself should **not** be in the Set, even if there is an edge from the node to itself. The method should return null for any invalid inputs, including: null values for the Graph or src; there is no node labeled src in the graph; distance less than 1. However, if distance is greater than or equal to 1 and there are no nodes within that distance (meaning: src is the only node in the graph), the method should return an empty Set.

**isHamiltonianPath:** Given a Graph, this method indicates whether the List of node values represents a Hamiltonian Path. A Hamiltonian Path is a valid path through the graph in which every node in the graph is visited exactly once, except for the start and end nodes, which are the same, so that it is a cycle. If the values in the input List represent a Hamiltonian Path, the method should return true, but the method should return false otherwise, e.g. if the path is not a cycle, if some nodes are not visited, if some nodes are visited more than once, if some values do not have corresponding nodes in the graph, if the input is not a valid path (i.e., there is a sequence of nodes in the List that are not connected by an edge), etc. The method should also return false if the input Graph or List is null.

For all of these, be sure to test your implementation with **both** directed **and** undirected graphs.

Please do not change the signature of any of the three methods, and please do not create any additional .java files for your solution; if you need additional classes, you can define them in _GraphUtils.java_. You may modify _BreadthFirstSearch.java_ and/or _DepthFirstSearch.java_ as part of your solution but please do not modify any of the other code that we distributed. Last, please be sure that all code is in the default package, i.e. there is no “package” declaration at the top of the source code.

## Helpful Hints

Resist the urge to look online for solutions! We are not asking you to derive any new algorithms or to “discover” something not covered in the lessons. Rather, you should try to apply the graph representations and traversal techniques that you have already learned.

You are free to use or even modify the code in the BreadthFirstSearch and DepthFirstSearch classes as needed for this assignment. You may find that you can simply use one implementation or the other without modification, or that there may be some implementation that you don’t need to use at all. These are just references for you to consider while writing these methods.

## Before You Submit

Please be sure that:

- your GraphUtils class is in the default package, i.e. there is no “package” declaration at the top of the source code
- your GraphUtils class compiles and you have not changed the signature of any of the three methods
- if you modified BreadthFirstSearch.java and/or DepthFirstSearch.java, the code compiles and is in the default package
- you have not created any additional .java files and have not made any changes to the other code we provided (you do not need to submit these files, and do not need to submit BreadthFirstSearch.java and DepthFirstSearch.java if you did not change them)

## Assessment

Your submission will be assessed using automatic grading scripts that will check that the methods work correctly for various inputs. Your score is determined by the percentage of these tests that “pass,” i.e. that produce the correct result for the specified input.

For each method, be sure that your implementation covers everything described in the specification, including error handling, and that you consider different categories or classes of inputs, e.g. when there are multiple paths between nodes for minDistance and nodesWithinDistance, when inputs do and do not represent Hamiltonian Paths, etc.

Before submitting your solution, you can run these grading scripts locally on your computer by following the steps below. These instructions assume you are using Eclipse, but should be applicable to other IDEs as well:

1. Download the JUnit distribution at [junit-dist.jar](https://courses.edx.org/assets/courseware/v1/2ed6e73287692ad54165a95ba8e5ac11/asset-v1:PennX+SD2x+2T2019+type@asset+block/junit-dist.jar) and save it in your project's root directory. You should be able to do this by dragging it from Finder/Explorer into Eclipse and dropping it in the folder that has the same name as your project. Then add it to the project's build path by right-clicking the file name in Eclipse to get the pop-up/context menu, then selecting "Build Path -->" and then "Add to Build Path."
2. Download the tests at [homework6-tests.jar](https://courses.edx.org/assets/courseware/v1/1688dfe80723c6be33d91e8a56bef157/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework6-tests.jar), and add it to the Eclipse project's build path as above.
3. Also download the test input files from [homework6-files.zip](https://courses.edx.org/assets/courseware/v1/35726903d5ce8f70b979cd5ea6be92cb/asset-v1:PennX+SD2x+2T2019+type@asset+block/homework6-files.zip). Unzip this file on your computer and copy the two .txt files into your Eclipse project; you should be able to drag and drop them right into Eclipse. Make sure you put them in your project's root directory, as you did with the two .jar files.
4. Now run the tests by right-clicking homework6-tests.jar in Eclipse to get the pop-up/context menu and selecting "Run As -->" and then "Java Application." You should see the tests run in the console and it should tell you your score for this assignment, or "Great job!" if your score would be 100%.

Alternatively, if you would like to run the autograder from the command line, put the two .jar files and your .class files for this assignment in the same directory along with the .txt files that you downloaded, and run:

**Mac/Linux:** java -cp .:junit-dist.jar:homework6-tests.jar Homework6Grader

**Windows:** java -cp .;junit-dist.jar;homework6-tests.jar Homework6Grader

This will add junit-dist.jar and homework6-tests.jar to the classpath and then run Java with Homework6Grader as the main class.
