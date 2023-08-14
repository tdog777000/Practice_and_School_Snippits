package Test_files.src;
import java.util.Scanner;
import java.util.ArrayList;

public class Blah {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int i = 1;
      String productName;
      int productPrice = 0;
      int productQuantity = 0;
      int item1Total = 0;
      int item2Total = 0;
      int cartTotal = 0;
      ArrayList<Class_test> itemList = new ArrayList<Class_test>();
      Class_test item1 = new Class_test();
      Class_test item2 = new Class_test();
      
      itemList.add(item1);
      itemList.add(item2);

      // Get item 1 and 2 details from user, create Class_test objects and place into arrayList
      for(Class_test items: itemList) {
            System.out.println("Item " + i);
            System.out.println("Enter the item name: ");
            productName = scnr.nextLine();
            System.out.println("Enter the item price: ");
            productPrice = scnr.nextInt();
            System.out.println("Enter the item quantity: ");
            productQuantity = scnr.nextInt();
            items.setName(productName);
            items.setPrice(productPrice);
            items.setQuantity(productQuantity);
            if (i == 1) {
               scnr.nextLine();
               i++;
               System.out.println();
               }
         }
      
      // Add costs of two items and print total
      item1Total = item1.getPrice() * item1.getQuantity();
      item2Total = item2.getPrice() * item2.getQuantity();
      // cartTotal = item one price + item two price
      cartTotal = item1Total + item2Total;
      // Total Cost
      System.out.println("\nTOTAL COST");
      // item one information
      item1.printItemPurchase();
      // item two information
      item2.printItemPurchase();
      System.out.println();
      // Total output
      System.out.println("Total: $" + cartTotal);
      
      return;
   }
}