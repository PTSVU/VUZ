package vuz.java.pract4;

public class Head {
    private String hairColor;

    public Head(String hairColor) {
        this.hairColor = hairColor;
    }

    public String getHairColor() {
        return hairColor;
    }

    public void setHairColor(String hairColor) {
        this.hairColor = hairColor;
    }

    public void talk(String message) {
        System.out.println("Голова говорит: " + message);
    }
}
