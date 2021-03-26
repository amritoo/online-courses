package week3.homework8;
/*
 * SD2x Homework #8
 * This class represents the Logic Tier in the three-tier architecture.
 * Implement the appropriate methods for this tier below.
 */

import java.util.HashSet;
import java.util.Set;

public class LogicTier {

    private DataTier dataTier; // link to the Data Tier

    public LogicTier(DataTier dataTier) {
        this.dataTier = dataTier;
    }

    /**
     * for a given name, search through all of the books and return the titles of those books whose author name includes the input name
     * <p>
     * findBookTitlesByAuthor should look for partial matches and should ignore case, i.e. be case-insensitive.
     * The titles of the books that are returned should be sorted based on the year they were published in
     * non-descending order; if two or more books have the same publication year, those books should be sorted alphabetically
     */
    public Set<String> findBookTitlesByAuthor(String authorName) {
        Set<Book> books = dataTier.getAllBooks();
        Set<String> titles = new HashSet<>();
        for (Book book : books) {
            if (containsString(book, authorName))
                titles.add(book.getTitle());
        }
        return titles;
    }

    private boolean containsString(Book book, String string) {
        String author = book.getAuthor().toLowerCase();
        return author.contains(string.toLowerCase());
    }

    /**
     * for a given year, search through all of the books and return the number of books published in that year
     */
    public int findNumberOfBooksInYear(int publishYear) {
        Set<Book> books = dataTier.getAllBooks();
        int count = 0;
        for (Book book : books) {
            if (book.getPublicationYear() == publishYear)
                count++;
        }
        return count;
    }

}
