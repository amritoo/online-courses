package week2.homework6;

import java.util.*;

/*
 * SD2x Homework #6
 * This is an implementation of Breadth First Search (BFS) on a graph.
 * You may modify and submit this code if you'd like.
 *
 * I edited this file
 */

public class BreadthFirstSearch {
	protected Set<Node> marked;
	protected Graph graph;
	protected Map<String, Integer> depthMap;

	public BreadthFirstSearch(Graph graphToSearch) {
		marked = new HashSet<>();
		graph = graphToSearch;
		depthMap = new HashMap<>(graphToSearch.getNumNodes());
	}
	
	/**
	 * This method was discussed in the lesson
	 */
	public boolean bfs(Node start, String elementToFind, boolean findOne) {
		if (!graph.containsNode(start)) {
				return false;
		}
		int level = 0;
		depthMap.put(start.getElement(), level);
		if (findOne && start.getElement().equals(elementToFind)) {
			return true;
		}
		Queue<Node> toExplore = new LinkedList<>();
		marked.add(start);
		toExplore.add(start);
		while (!toExplore.isEmpty()) {
			Node current = toExplore.remove();
			level = depthMap.get(current.getElement()) + 1;
			for (Node neighbor : graph.getNodeNeighbors(current)) {
				if (!marked.contains(neighbor)) {
					depthMap.put(neighbor.getElement(), level);
					if (findOne && neighbor.getElement().equals(elementToFind)) {
						return true;
					}
					marked.add(neighbor);
					toExplore.add(neighbor);
				}
			}
		}
		return false;
	}

	public int depthOfNode(Node start, String elementToFind) {
		if(start == null || elementToFind == null || !bfs(start, elementToFind, true))
			return -1;
		return depthMap.get(elementToFind);
	}

	public Set<String> getNumberOfNodes(Node start, int distance) {
		if (distance <= 0)
			return null;
		bfs(start, "NOTHING", false);
		Set<String> nodes = new HashSet<>();
		for(String string : depthMap.keySet()) {
			if(depthMap.get(string) <= distance)
				nodes.add(string);
		}
		nodes.remove(start.getElement());
		return nodes;
	}

}
