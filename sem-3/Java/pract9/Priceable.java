package vuz.java.pract9;

interface Priceable {
    double getPrice();
}

class Car implements Priceable {
    private double price;

    public Car(double price) {
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }
}

class Laptop implements Priceable {
    private double price;

    public Laptop(double price) {
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }
}

