package week3.homework8;
/*
 * SD2x Homework #8
 * This class represents the Presentation Tier in the three-tier architecture.
 * Implement the appropriate methods for this tier below.
 * Also implement the start method as described in the assignment description.
 */

import java.util.Scanner;
import java.util.Set;

public class PresentationTier {

    private LogicTier logicTier; // link to the Logic Tier

    public PresentationTier(LogicTier logicTier) {
        this.logicTier = logicTier;
    }

    /**
     * asks the user which feature they would like to use and invokes the appropriate methods in the appropriate classes.
     * Once the output has been displayed, the program should terminate
     */
    public void start() {
        System.out.println("Select one of the following:");
        System.out.println("\t1. show book titles by author");
        System.out.println("\t2. show number of books published in a given year");
        System.out.print("Enter a number: ");
        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();
        switch (choice) {
            case 1:
                showBookTitlesByAuthor();
                break;
            case 2:
                showNumberOfBooksInYear();
                break;
            default:
                System.out.println("Input must be either 1 or 2");
        }
    }

    /**
     * using the command-line (i.e., reading from System.in), ask the user to enter part or all of an author’s name,
     * then display (using System.out) the titles of those books whose author name includes the input name
     * <p>
     * showBookTitlesByAuthor should look for partial matches and should ignore case, i.e. be case-insensitive.
     * The titles of the books that are displayed should be sorted based on the year they were published in
     * non-descending order; if two or more books have the same publication year, those books should be sorted alphabetically
     */
    public void showBookTitlesByAuthor() {
        System.out.println("\n\n");
        System.out.println("Enter part or all of an author’s name.");
        System.out.print("Name: ");
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        Set<String> books = logicTier.findBookTitlesByAuthor(name);
        if (books == null || books.size() < 1) {
            System.out.println("No books found!");
            return;
        }
        System.out.println(books.size() + " books found!");
        for (String book : books) {
            System.out.println(book);
        }
    }

    /**
     * using the command-line (i.e., reading from System.in), ask the user to enter a year,
     * then display (using System.out) the number of books published in that year
     */
    public void showNumberOfBooksInYear() {
        System.out.println("\n\n");
        System.out.println("Enter enter a year.");
        System.out.print("Year: ");
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        int number = logicTier.findNumberOfBooksInYear(year);
        System.out.println("Total books published in year " + year + " is: " + number);
    }

}
