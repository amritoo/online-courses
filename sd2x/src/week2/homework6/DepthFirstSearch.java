package week2.homework6;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * SD2x Homework #6
 * This is an implementation of Depth First Search (DFS) on a graph.
 * You may modify and submit this code if you'd like.
 *
 * I edited it for hamilton graph
 */

public class DepthFirstSearch {
    protected Set<Node> marked;
    protected Graph graph;

    public DepthFirstSearch(Graph graphToSearch) {
        marked = new HashSet<Node>();
        graph = graphToSearch;
    }

    public boolean dfs(Node start, String elementToFind) {
        if (!graph.containsNode(start)) {
            return false;
        }

        if (start.getElement().equals(elementToFind)) {
            return true;
        } else {
            marked.add(start);
            for (Node neighbor : graph.getNodeNeighbors(start)) {
                if (!marked.contains(neighbor) && dfs(neighbor, elementToFind))
                    return true;
            }
            return false;
        }
    }

    private boolean isValid(List<String> values) {
        for (String value : values) {
            if (!graph.containsElement(value))
                return false;
        }
        return true;
    }

    private boolean connectEdge(Node start, Node end) {
        if (marked.contains(start))
            return false;
        marked.add(start);
        Set<Node> neighbour = graph.getNodeNeighbors(start);
        return neighbour.contains(end);
    }

    public boolean isHamilton(List<String> values) {
        if (values == null || values.size() == 0 || !isValid(values))
            return false;

        Node startNode = graph.getNode(values.get(0));
        Node lastNode = graph.getNode(values.get(values.size() - 1));
        if (startNode != lastNode)
            return false;

        Node current = startNode;
        int index = 1;
        while (index < values.size() - 1) {
            Node next = graph.getNode(values.get(index));
            index++;
            if (!connectEdge(current, next))
                return false;
            current = next;
        }

        return connectEdge(current, lastNode) && marked.size() == graph.getNumNodes();
    }

}