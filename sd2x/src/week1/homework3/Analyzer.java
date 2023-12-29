package week1.homework3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/*
 * SD2x Homework #3
 * Implement the methods below according to the specification in the assignment description.
 * Please be sure not to change the method signatures!
 */
public class Analyzer {

    /*
     * Implement this method in Part 1
     */
    public static List<Sentence> readFile(String filename) {
        List<Sentence> sentences = new LinkedList<>();

        if (filename == null) {
            return sentences;
        }
        File file = new File(filename);
        if (file.exists()) {
            try {
                Scanner scanner = new Scanner(file);
                while (scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    if (isValid(line)) {
                        int index = line.indexOf(" ");
                        String num = line.substring(0, index);
                        int score = Integer.parseInt(num);
                        String text = line.substring(index + 1);
                        sentences.add(new Sentence(score, text));
                    }
                }
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
        return sentences;
    }

    private static boolean isValid(String line) {
        ArrayList<String> valid = new ArrayList<>();
        valid.add("-2");
        valid.add("-1");
        valid.add("0");
        valid.add("1");
        valid.add("2");
        int ind = line.indexOf(" ");
        if (ind < 1 || ind >= line.length() - 1 || line.charAt(ind + 1) == ' ')
            return false;
        String[] words = line.split(" ");
        if (words.length <= 1 || !valid.contains(words[0])) {
            return false;
        }
        return true;
    }

    /*
     * Implement this method in Part 2
     */
    public static Set<Word> allWords(List<Sentence> sentences) {
        Set<Word> words = new HashSet<>();

        if (sentences == null || sentences.size() == 0)
            return words;

        ArrayList<Word> wordArrayList = new ArrayList<>();
        for (Sentence sentence : sentences) {
            if (sentence != null) {
                ArrayList<String> validWords = parseValidWords(sentence.getText());
                for (String s : validWords) {
                    Word word = new Word(s);
                    int index = wordArrayList.indexOf(word);
                    if (index >= 0) {
                        wordArrayList.get(index).increaseTotal(sentence.getScore());
                    } else {
                        word.increaseTotal(sentence.getScore());
                        wordArrayList.add(word);
                    }
                }
            }
        }

        words.addAll(wordArrayList);
        return words;
    }

    private static ArrayList<String> parseValidWords(String text) {
        ArrayList<String> words = new ArrayList<>();

        if (text == null || text.equals(""))
            return words;

        String[] w = text.split(" ");
        for (String s : w) {
            if (Character.isLetter(s.charAt(0))) {
                words.add(s.toLowerCase());
            }
        }
        return words;
    }

    /*
     * Implement this method in Part 3
     */
    public static Map<String, Double> calculateScores(Set<Word> words) {
        Map<String, Double> map = new HashMap<>();

        if (words == null || words.size() == 0)
            return map;

        for (Word word : words) {
            if (word != null) {
                map.put(word.getText(), word.calculateScore());
            }
        }

        return map;
    }

    /*
     * Implement this method in Part 4
     */
    public static double calculateSentenceScore(Map<String, Double> wordScores, String sentence) {
        ArrayList<String> arrayList = parseValidWords(sentence);

        if (wordScores == null || wordScores.size() == 0 || arrayList.size() == 0)
            return 0;

        double total = 0;
        for (String w : arrayList) {
            total += wordScores.getOrDefault(w, 0.0);
        }
        return total / arrayList.size();
    }

    /*
     * This method is here to help you run your program. Y
     * You may modify it as needed.
     */
    public static void main(String[] args) {
        System.out.print("Please enter a sentence: ");
        Scanner in = new Scanner(System.in);
        String sentence = in.nextLine();
        in.close();

        List<Sentence> sentences = Analyzer.readFile("src/week1/homework3/reviews.txt");
        Set<Word> words = Analyzer.allWords(sentences);
        Map<String, Double> wordScores = Analyzer.calculateScores(words);

        double score = Analyzer.calculateSentenceScore(wordScores, sentence);

        System.out.println("The sentiment score is " + score);
    }
}
