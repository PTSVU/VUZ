package vuz.java.pract4;

public class Leg {
    private int lengthInCm;

    public Leg(int lengthInCm) {
        this.lengthInCm = lengthInCm;
    }

    public int getLengthInCm() {
        return lengthInCm;
    }

    public void setLengthInCm(int lengthInCm) {
        this.lengthInCm = lengthInCm;
    }

    public void walk() {
        System.out.println("Нога идет");
    }
}
