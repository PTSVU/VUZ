package vuz.java.pract1;

import java.util.ArrayList;
import java.util.Scanner;

public class ArrMinMax extends Base {

    public ArrMinMax() {
        super(4);
    }

    public static void main(String[] args) {
        ArrMinMax ArrSum = new ArrMinMax();
        ArrayList<Integer> num = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        num = vuz.java.pract1.ArrSum.int_input(scanner);
        long sum = 0, min = 0, max = 0;
        int i = 0;
        while (i < num.size()) {
            if (i == 0) {
                min = num.get(i);
                max = num.get(i);
            }
            sum += num.get(i);
            if (num.get(i) < min) {
                min = num.get(i);
            }
            if (num.get(i) > max) {
                max = num.get(i);
            }
            i++;
        }
        System.out.println("Сумма: " + sum + "\nМинимальное: " + min + "\nМаксимальное: " + max + "\n\n");
    }
}
