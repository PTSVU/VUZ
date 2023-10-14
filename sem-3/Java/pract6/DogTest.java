package vuz.java.pract6;

public class DogTest {
    public static void main(String[] args) {
        Dog labrador = new Labrador("Max", 3);
        Dog bulldog = new Bulldog("Rock", 5);

        System.out.println(labrador);
        labrador.bark();

        System.out.println(bulldog);
        bulldog.bark();
    }
}
