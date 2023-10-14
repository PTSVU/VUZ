package vuz.java.pract4;

public class CircleTest {
    public static void main(String[] args) {
        Circle circle = new Circle(5.0);
        System.out.println("Радиус окружности: " + circle.getRadius());
        System.out.println("Площадь окружности: " + circle.calculateArea());
        System.out.println("Длина окружности: " + circle.calculateCircumference());
        try {
            circle.setRadius(-2.0);
        } catch (IllegalArgumentException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
        circle.setRadius(3.0);
        System.out.println("Новый радиус окружности: " + circle.getRadius());
        System.out.println("Новая площадь окружности: " + circle.calculateArea());
        System.out.println("Новая длина окружности: " + circle.calculateCircumference());
    }
}
