package Test_files.src;

public class Class_test {

    //Private fields - itemName, itemPrice, and itemQuanity
    private String itemName;
    private int itemPrice;
    private int itemQuantity;
 
    /*Default Constructor
     itemName - Initialized to "none"
     itemPrice - Initialized to 0
     itemQuantity - Initialized to 0
    */
    public Class_test() {
       itemName = "none";
       itemPrice = 0;
       itemQuantity = 0;
    }
     
    //public member methods (mutators & accessors)
    
    //mutator = setName() & accessor = getName()
    public void setName(String product) {
       itemName = product;   
    }
    
    public String getName() {
       return itemName;   
    }
    
    //setPrice() & getPrice() 
    public void setPrice(int price) {
       itemPrice = price;
    }
    
    public int getPrice() {
       return itemPrice;   
    }
    
    //setQuantity() & getQuantity() 
    public void setQuantity(int quantity) {
       itemQuantity = quantity;
    }
    
    public int getQuantity() {
       return itemQuantity;
    }
    
   //print item to purchase
   public void printItemPurchase() {
      System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice +  
                         " = $" + (itemPrice * itemQuantity));
   }
}
 