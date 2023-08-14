package Programs.src;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Sent_sep {
    public static void main(String[] args) throws FileNotFoundException {
        String[] sentences;
        FileInputStream paragraph = new FileInputStream("Paragraph.txt");
        try (Scanner fileInput = new Scanner(paragraph)) {
            String fullText = fileInput.nextLine();
            System.out.println();
            System.out.println();
            System.out.println(fullText);
            sentences = fullText.split("\\. |\\? |\\! "); //Changed argument
            System.out.println();
            System.out.println();
            System.out.println();
        }

         for (int x = 0; x < (sentences.length); x++){
            if (sentences[x].isEmpty() != true){
                System.out.println(sentences[x].strip() + "."); //Changed to add periods
            }
        }

        /*CREATE A FILE TO PASTE THE PARAGRAPH. OPEN THE FILE AND STORE INTO INPUT STREAM USING "FileInputStream" 

           USE PROGRAM TO FIND ". "  OR  "? "  OR  "! " STRINGS AND STORE THE STRING BEFORE THAT INTO ELEMENTS OF AN ARRAY "sentences"
           PRINT THE ELEMENTS, EACH ON A NEW LINE, TO COPY INTO EMAILS.

           SEND THIS PROGRAM TO WORK LAPTOP VIA CITIZENS EMAIL. COPY PARAGRAPH INTO THE TXT FILE TO READ FROM.
           RUN PROGRAM. GUCCI.
        */
        return;
    }
    
}
