package vuz.java.pract4;

public class Circle {
    private double radius;

    public Circle(double radius) {
        setRadius(radius);
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        if (radius >= 0) {
            this.radius = radius;
        } else {
            throw new IllegalArgumentException("Радиус не может быть отрицательным");
        }
    }

    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    public double calculateCircumference() {
        return 2 * Math.PI * radius;
    }
}
