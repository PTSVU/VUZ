package vuz.java.pract1;

import java.util.Scanner;
import java.util.ArrayList;
public class ArrSum extends Base {

    public ArrSum() {
        super(3);
    }

    public static void main(String[] args) {
        ArrSum ArrSum = new ArrSum();
        ArrayList<Integer> num = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        num = int_input(scanner);
        long sum = 0;
        for (int i : num) {
            sum += i;
        }

        double aver = (double) sum / num.size();
        System.out.println("Сумма: " + sum);
        System.out.println("Среднее арифметическое: " + aver + "\n\n");
    }

    public static ArrayList<Integer> int_input(Scanner scanner) {

        ArrayList<Integer> num = new ArrayList<>();

        System.out.print("Введите целое число (или \"ё\" или \"`\" для завершения): ");
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("ё") || input.equals("`")) {
                break;
            }
            try {
                int number = Integer.parseInt(input);
                num.add(number);
            } catch (NumberFormatException e) {
                System.out.println("Не число");
            }
        }
        return num;
    }
}
