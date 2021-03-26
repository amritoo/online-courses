package week2.homework6;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * SD2x Homework #6
 * Implement the methods below according to the specification in the assignment description.
 * Please be sure not to change the signature of any of the methods!
 */

public class GraphUtils {

    public static int minDistance(Graph graph, String src, String dest) {
        if (graph == null || src == null || dest == null ||
                !graph.containsElement(src) || !graph.containsElement(dest))
            return -1;
        BreadthFirstSearch breadthFirstSearch = new BreadthFirstSearch(graph);
        int depth = breadthFirstSearch.depthOfNode(graph.getNode(src), dest);
        return depth >= 0 ? depth : -1;
    }


    public static Set<String> nodesWithinDistance(Graph graph, String src, int distance) {
        if (graph == null || src == null || !graph.containsElement(src) || distance < 1)
            return null;
        BreadthFirstSearch breadthFirstSearch = new BreadthFirstSearch(graph);
        return breadthFirstSearch.getNumberOfNodes(graph.getNode(src), distance);
    }


    public static boolean isHamiltonianPath(Graph g, List<String> values) {
        if (g == null || values == null) {
            return false;
        }
        DepthFirstSearch depthFirstSearch = new DepthFirstSearch(g);
        return depthFirstSearch.isHamilton(values);
    }

}
