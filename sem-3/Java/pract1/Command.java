package vuz.java.pract1;

public class Command extends Base {
    public Command() {
        super(5);
    }

    public static void main(String[] args) {
        Command Command = new Command();
        for (int i = 1; i <= 9; i++) {
            System.out.println("Аргумент " + i);
        }
        System.out.println("\n");
    }
}
