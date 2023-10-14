package vuz.java.pract2;

import java.util.Objects;

class Circle {
    private double radius;

    public Circle(double radius) {
        if (radius <= 0) {
            throw new IllegalArgumentException("Радиус окружности должен быть положительным числом.");
        }
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        if (radius <= 0) {
            throw new IllegalArgumentException("Радиус окружности должен быть положительным числом.");
        }
        this.radius = radius;
    }

    public double calculateArea() {
        return Math.PI * Math.pow(radius, 2);
    }

    public double calculateCircumference() {
        return 2 * Math.PI * radius;
    }

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Circle circle = (Circle) o;
        return Double.compare(circle.radius, radius) == 0;
    }

    public int hashCode() {
        return Objects.hash(radius);
    }
}

class CircleTest {
    public static void main(String[] args) {
        Circle circle1 = new Circle(5.0);
        Circle circle2 = new Circle(7.5);

        System.out.println("Окружность 1:");
        System.out.println("Радиус: " + circle1.getRadius());
        System.out.println("Площадь: " + circle1.calculateArea());
        System.out.println("Длина окружности: " + circle1.calculateCircumference());

        System.out.println("\nОкружность 2:");
        System.out.println("Радиус: " + circle2.getRadius());
        System.out.println("Площадь: " + circle2.calculateArea());
        System.out.println("Длина окружности: " + circle2.calculateCircumference());

        if (circle1.equals(circle2)) {
            System.out.println("\nОкружности равны по радиусу.");
        } else {
            System.out.println("\nОкружности разные по радиусу.");
        }
    }
}
