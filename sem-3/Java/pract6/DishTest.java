package vuz.java.pract6;

public class DishTest {
    public static void main(String[] args) {
        Dish plate = new Plate("ceramic");
        Dish cup = new Cup("glass");

        System.out.println(plate);
        plate.use();

        System.out.println(cup);
        cup.use();
    }
}
