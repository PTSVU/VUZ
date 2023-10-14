package vuz.java.pract4;

public class BookTest {
    public static void main(String[] args) {
        Book book1 = new Book("Yes", "Yep", 1999, ")))");
        Book book2 = new Book("No", "Nope", 1998, "(((");

        System.out.println("Book 1: " + book1);
        System.out.println("Book 2: " + book2);

        book1.setTitle("YEE");
        book1.setYear(2000);

        System.out.println("Updated Book 1: " + book1);
    }
}
