package vuz.java.pract9;

public class PriceableTest {
    public static void main(String[] args) {
        Priceable car = new Car(25000.0);
        Priceable laptop = new Laptop(1200.0);

        System.out.println("Car price: $" + car.getPrice());
        System.out.println("Laptop price: $" + laptop.getPrice());
    }
}
