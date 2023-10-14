package vuz.java.pract4;

public class HumanTest {
    public static void main(String[] args) {
        Head head = new Head("Да");
        Leg leftLeg = new Leg(75);
        Leg rightLeg = new Leg(75);
        Hand leftHand = new Hand(5);
        Hand rightHand = new Hand(5);

        Human human = new Human(head, leftLeg, rightLeg, leftHand, rightHand);

        human.doHumanThings();
    }
}
