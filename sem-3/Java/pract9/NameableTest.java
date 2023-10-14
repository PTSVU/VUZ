package vuz.java.pract9;

public class NameableTest {
    public static void main(String[] args) {
        Nameable planet = new Planet("Earth");
        Nameable animal = new Animal("Lion");

        System.out.println("Planet name: " + planet.getName());
        System.out.println("Animal name: " + animal.getName());
    }
}
