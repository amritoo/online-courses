package week2.homework5;
/*
 * SD2x Homework #5
 * Implement the method below according to the specification in the assignment description.
 * Please be sure not to change the method signature!
 */

import java.util.List;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class MovieRatingsParser {

    public static TreeMap<String, PriorityQueue<Integer>> parseMovieRatings(List<UserMovieRating> allUsersRatings) {
        TreeMap<String, PriorityQueue<Integer>> treeMap = new TreeMap<>();

        if (allUsersRatings == null || allUsersRatings.size() == 0)
            return treeMap;
        for (UserMovieRating userMovieRating : allUsersRatings) {
            if (!isValid(userMovieRating))
                continue;
            String title = userMovieRating.getMovie().toLowerCase();
            PriorityQueue<Integer> ratings = treeMap.get(title);
            if (ratings == null) {
                ratings = new PriorityQueue<>();
            }
            ratings.add(userMovieRating.getUserRating());
            treeMap.put(title, ratings);
        }
        return treeMap;
    }

    private static boolean isValid(UserMovieRating userMovieRating) {
        if (userMovieRating == null ||
                userMovieRating.getMovie() == null ||
                userMovieRating.getMovie().length() == 0 ||
                userMovieRating.getUserRating() < 0)
            return false;
        return true;
    }

}
