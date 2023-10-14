package vuz.java.pract1;

public class Harmonic extends Base {
    public Harmonic() {
        super(6);
    }

    public static void main(String[] args) {
        Harmonic Harmonic = new Harmonic();
        for (int i = 1; i <= 10; i++) {
            double harmonicNumber = 1.0 / i;
            System.out.printf("Число %d: %.10f\n", i, harmonicNumber);
        }
        System.out.println("\n");
    }
}
