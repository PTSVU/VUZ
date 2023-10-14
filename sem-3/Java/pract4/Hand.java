package vuz.java.pract4;

public class Hand {
    private int fingersCount;

    public Hand(int fingersCount) {
        this.fingersCount = fingersCount;
    }

    public int getFingersCount() {
        return fingersCount;
    }

    public void setFingersCount(int fingersCount) {
        this.fingersCount = fingersCount;
    }

    public void wave() {
        System.out.println("Рука машет");
    }
}
