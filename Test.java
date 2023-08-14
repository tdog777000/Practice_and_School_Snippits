package Test_files.src;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Test {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double wallHeight = 0.0;
        double wallWidth = 0.0;
        double wallArea = 0.0;
        double gallonsPaintNeeded = 0.0;
        boolean notValid = true;
        
        final double squareFeetPerGallons = 350.0;
        
        // Implement a do-while loop to ensure input is valid
        // Prompt user to input wall's height
        do {
            System.out.println("Enter wall height (feet): ");

            try {
                wallHeight = scnr.nextDouble(); // Grabs input from user.
                notValid = false;
            } 
            catch (InputMismatchException e) { // Performs statements below if mismatch exception is thrown.
                scnr.nextLine();
                System.out.println("Enter input as numerical digits.");
            }
            /* If data type is valid and input is not positive, value of "notValid" is changed back to true.
            This causes the condition for the loop to pass and triggers another iteration for user input.*/
            if (notValid == false && wallHeight <= 0) {
                notValid = true;
                System.out.println("Must enter a positive number.");
            }
        }
        while (notValid); //Loops if notValid is true


        // Implement a do-while loop to ensure input is valid
        // Prompt user to input wall's width
        do {
            System.out.println("Enter wall width (feet): ");
            try {
                wallWidth = scnr.nextDouble(); // Grabs input from user.
                notValid = false;
            } 
            catch (InputMismatchException e) { // Performs statements below if mismatch exception is thrown.
                scnr.nextLine();
                System.out.println("Enter input as numerical digits.");
            }
            /* If data type is valid and input is not positive, value of "notValid" is changed back to true.
            This causes the condition for the loop to pass and triggers another iteration for user input.*/
            if (notValid == false && wallWidth <= 0) {
                notValid = true;
                System.out.println("Must enter a positive number.");
            }
        }
        while (notValid); //Loops if notValid is true


        // Calculate and output wall area
        wallArea = wallHeight * wallWidth;
        System.out.println("Wall area: " + wallArea + " square feet");


        // Calculate and output the amount of paint (in gallons) needed to paint the wall
        gallonsPaintNeeded = wallArea/squareFeetPerGallons;
        System.out.println("Paint needed: " + gallonsPaintNeeded + " gallons");

    }
}
