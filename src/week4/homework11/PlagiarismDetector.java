package week4.homework11;

import java.io.File;
import java.util.*;

/*
 * SD2x Homework #11
 * Improve the efficiency of the code below according to the guidelines in the assignment description.
 * Please be sure not to change the signature of the detectPlagiarism method!
 * However, you may modify the signatures of any of the other methods as needed.
 */

public class PlagiarismDetector {

    private static Map<String, Set<String>> result;

    public static Map<String, Integer> detectPlagiarism(String dirName, int windowSize, int threshold) {
        File dirFile = new File(dirName);
        String[] files = dirFile.list();

        Map<String, Integer> numberOfMatches = new HashMap<>();

        result = new HashMap<>();
        for (String file1 : files) {

            String dir1 = dirName + "/" + file1;
            Set<String> file1Phrases;
            if (result.containsKey(dir1)) {
                file1Phrases = result.get(dir1);
            } else {
                file1Phrases = createPhrases(dir1, windowSize);
                result.put(dir1, file1Phrases);
            }
            if (file1Phrases == null)
                return null;

            for (String file2 : files) {

                String dir2 = dirName + "/" + file2;
                Set<String> file2Phrases;
                if (result.containsKey(dir2)) {
                    file2Phrases = result.get(dir2);
                } else {
                    file2Phrases = createPhrases(dir2, windowSize);
                    result.put(dir2, file2Phrases);
                }
                if (file2Phrases == null)
                    return null;
                Set<String> matches = findMatches(file1Phrases, file2Phrases);

                if (matches.size() > threshold) {
                    String key = file1 + "-" + file2;
                    if (!numberOfMatches.containsKey(file2 + "-" + file1) && !file1.equals(file2)) {
                        numberOfMatches.put(key, matches.size());
                    }
                }
            }

        }

        return sortResults(numberOfMatches);

    }


    /*
     * This method reads the given file and then converts it into a Collection of Strings.
     * It does not include punctuation and converts all words in the file to uppercase.
     */
    protected static List<String> readFile(String filename) {
        if (filename == null) return null;

        List<String> words = new ArrayList<>();

        try {
            Scanner in = new Scanner(new File(filename));
            while (in.hasNext()) {
                words.add(in.next().replaceAll("[^a-zA-Z]", "").toUpperCase());
            }
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }

        return words;
    }


    /*
     * This method reads a file and converts it into a Set/List of distinct phrases,
     * each of size "window". The Strings in each phrase are whitespace-separated.
     */
    protected static Set<String> createPhrases(String filename, int window) {

        if (filename == null || window < 1) return null;

        List<String> words = readFile(filename);
        if (words == null) return null;

        Set<String> phrases = new HashSet<>();

        for (int i = 0; i < words.size() - window + 1; i++) {
            StringBuilder phrase = new StringBuilder();
            for (int j = 0; j < window; j++) {
                phrase.append(words.get(i + j)).append(" ");
            }
            phrases.add(phrase.toString());
        }

        return phrases;
    }


    /*
     * Returns a Set of Strings that occur in both of the Set parameters.
     * However, the comparison is case-insensitive.
     */
    protected static Set<String> findMatches(Set<String> myPhrases, Set<String> yourPhrases) {

        Set<String> matches = new HashSet<>();

        if (myPhrases != null && yourPhrases != null) {

            for (String mine : myPhrases) {
                if (yourPhrases.contains(mine)) {
                    matches.add(mine);
                }
            }
        }
        return matches;
    }

    /*
     * Returns a LinkedHashMap in which the elements of the Map parameter
     * are sorted according to the value of the Integer, in non-ascending order.
     */
    protected static LinkedHashMap<String, Integer> sortResults(Map<String, Integer> possibleMatches) {

        // Because this approach modifies the Map as a side effect of printing
        // the results, it is necessary to make a copy of the original Map
        Map<String, Integer> copy = new HashMap<>(possibleMatches);

        LinkedHashMap<String, Integer> list = new LinkedHashMap<>();

        for (int i = 0; i < copy.size(); i++) {
            int maxValue = 0;
            String maxKey = null;
            for (String key : copy.keySet()) {
                if (copy.get(key) > maxValue) {
                    maxValue = copy.get(key);
                    maxKey = key;
                }
            }

            list.put(maxKey, maxValue);

            copy.put(maxKey, -1);
        }

        //TODO: improve sorting
        ArrayList<Integer> integers = new ArrayList<>(possibleMatches.values());
        integers.sort(Comparator.reverseOrder());

        return list;
    }

    /*
     * This method is here to help you measure the execution time and get the output of the program.
     * You do not need to consider it for improving the efficiency of the detectPlagiarism method.
     */
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please specify the name of the directory containing the corpus.");
            System.exit(0);
        }
        String directory = args[0];
        long start = System.currentTimeMillis();
        Map<String, Integer> map = PlagiarismDetector.detectPlagiarism(directory, 4, 5);
        long end = System.currentTimeMillis();
        double timeInSeconds = (end - start) / (double) 1000;
        System.out.println("Execution time (wall clock): " + timeInSeconds + " seconds");
        Set<Map.Entry<String, Integer>> entries = map.entrySet();
        for (Map.Entry<String, Integer> entry : entries) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

}
