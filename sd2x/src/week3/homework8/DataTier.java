package week3.homework8;
/*
 * SD2x Homework #8
 * This class represents the Data Tier in the three-tier architecture.
 * Implement the appropriate methods for this tier below.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DataTier {

    private String fileName; // the name of the file to read

    public DataTier(String inputSource) {
        fileName = inputSource;
    }

    /**
     * read the data file containing information about the books, create Book objects for each, and then return the Book objects
     */
    public Set<Book> getAllBooks() {
        Set<Book> books = new HashSet<>();
        if (fileName == null)
            return books;
        File file = new File(fileName);
        if (file.exists()) {
            try {
                Scanner scanner = new Scanner(file);
                while (scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    Book book = parseBook(line);
                    books.add(book);
                }
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
        return books;
    }

    /**
     * line = [title][tab][author][tab][year]
     */
    private Book parseBook(String line) {
        String[] strings = line.split("\t");
        if (strings.length == 3) {
            String title = strings[0];
            String author = strings[1];
            String year = strings[2];
            Book book = new Book(title, author, Integer.parseInt(year));
            return book;
        }
        return null;
    }

}
