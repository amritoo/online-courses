package week2.homework5;
/*
 * SD2x Homework #5
 * Implement the methods below according to the specification in the assignment description.
 * Please be sure not to change the method signatures!
 */

import java.util.*;


public class MovieRatingsProcessor {

    public static List<String> getAlphabeticalMovies(TreeMap<String, PriorityQueue<Integer>> movieRatings) {
        if (movieRatings == null || movieRatings.size() == 0)
            return new ArrayList<>();
        Set<String> movieSet = movieRatings.keySet();
        return new ArrayList<>(movieSet);
    }

    public static List<String> getAlphabeticalMoviesAboveRating(TreeMap<String, PriorityQueue<Integer>> movieRatings, int rating) {
        List<String> movies = new ArrayList<>();
        if (movieRatings == null || movieRatings.size() == 0)
            return movies;
//        List<String> movieTitles = new ArrayList<>(movieRatings.keySet());
        Set<String> movieSet = movieRatings.keySet();
        for (String title : movieSet) {
            PriorityQueue<Integer> ratings = movieRatings.get(title);
            if (!ratings.isEmpty() && ratings.peek() > rating)
                movies.add(title);
        }
        return movies;
    }

    public static TreeMap<String, Integer> removeAllRatingsBelow(TreeMap<String, PriorityQueue<Integer>> movieRatings, int rating) {
        TreeMap<String, Integer> movies = new TreeMap<>();
        if (movieRatings == null || movieRatings.size() == 0) {
            return movies;
        }
//        List<String> movieTitles = new ArrayList<>(movieRatings.keySet());
        Set<String> movieSet = movieRatings.keySet();
        for (String title : movieSet) {
            PriorityQueue<Integer> ratings = movieRatings.get(title);
            int count = 0;
            while (!ratings.isEmpty() && ratings.peek() < rating) {
                ratings.remove();
                count++;
            }
            if (ratings.isEmpty()) {
                movieRatings.remove(title);
            }
            if (count > 0) {
                movies.put(title, count);
            }
        }
        return movies;
    }
}
