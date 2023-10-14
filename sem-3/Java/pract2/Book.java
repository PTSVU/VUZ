package vuz.java.pract2;

import java.util.Arrays;

class Book {
    private String author;
    private String title;
    private int year;

    public Book(String author, String title, int year) {
        this.author = author;
        this.title = title;
        this.year = year;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public String toString() {
        return author + " - " + title + " (" + year + ")";
    }
}

class Bookshelf {
    private Book[] books;
    private int numberOfBooks;

    public Bookshelf(int capacity) {
        books = new Book[capacity];
        numberOfBooks = 0;
    }

    public void addBook(Book book) {
        if (numberOfBooks < books.length) {
            books[numberOfBooks] = book;
            numberOfBooks++;
        } else {
            System.out.println("Книжная полка заполнена, нельзя добавить больше книг.");
        }
    }

    public Book getEarliestBook() {
        if (numberOfBooks == 0) {
            return null;
        }

        Book earliestBook = books[0];
        for (int i = 1; i < numberOfBooks; i++) {
            if (books[i].getYear() < earliestBook.getYear()) {
                earliestBook = books[i];
            }
        }
        return earliestBook;
    }

    public Book getLatestBook() {
        if (numberOfBooks == 0) {
            return null;
        }

        Book latestBook = books[0];
        for (int i = 1; i < numberOfBooks; i++) {
            if (books[i].getYear() > latestBook.getYear()) {
                latestBook = books[i];
            }
        }
        return latestBook;
    }

    public void sortBooksByYear() {
        Arrays.sort(books, 0, numberOfBooks, (book1, book2) -> Integer.compare(book1.getYear(), book2.getYear()));
    }

    public void printBooks() {
        System.out.println("Список книг на книжной полке:");
        for (int i = 0; i < numberOfBooks; i++) {
            System.out.println(books[i]);
        }
    }
}

class BookTest {
    public static void main(String[] args) {
        Book book1 = new Book("Автор1", "Книга1", 2000);
        Book book2 = new Book("Автор2", "Книга2", 1995);
        Book book3 = new Book("Автор3", "Книга3", 2010);

        Bookshelf bookshelf = new Bookshelf(5);

        bookshelf.addBook(book1);
        bookshelf.addBook(book2);
        bookshelf.addBook(book3);

        bookshelf.printBooks();

        Book earliestBook = bookshelf.getEarliestBook();
        Book latestBook = bookshelf.getLatestBook();

        if (earliestBook != null) {
            System.out.println("Самая ранняя книга: " + earliestBook);
        } else {
            System.out.println("На книжной полке нет книг.");
        }

        if (latestBook != null) {
            System.out.println("Самая поздняя книга: " + latestBook);
        } else {
            System.out.println("На книжной полке нет книг.");
        }

        bookshelf.sortBooksByYear();
        bookshelf.printBooks();
    }
}
