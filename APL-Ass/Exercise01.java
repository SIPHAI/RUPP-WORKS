import java.util.Scanner; // import the Scanner class 

class Exercise1 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    String userName;
    
    // Enter username and press Enter
    System.out.println("Enter Your Name:"); 
    userName = myObj.nextLine();   
       
    System.out.println("Hello: " + userName);        
  }
}
