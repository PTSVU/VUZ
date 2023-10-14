package vuz.java.pract5;

public class MovableRectangleTest {
    public static void main(String[] args) {
        MovableRectangle rect = new MovableRectangle(1, 2, 4, 6, 2, 2);

        System.out.println("Initial Rectangle: " + rect);
        System.out.println("Do both points have the same speed? " + rect.sameSpeed());

        rect.moveUp();
        System.out.println("Rectangle after moving up: " + rect);

        rect.moveRight();
        System.out.println("Rectangle after moving right: " + rect);

        System.out.println("Do both points have the same speed? " + rect.sameSpeed());
    }
}
