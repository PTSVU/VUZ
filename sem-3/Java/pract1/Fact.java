package vuz.java.pract1;

import java.util.Scanner;
import java.math.BigInteger;



public class Fact extends Base {
    public Fact() {
        super(7);
    }

    public static void main(String[] args) {
        Fact Fact = new Fact();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите число: ");
        int num = scanner.nextInt();
        BigInteger fact = calcFact(num);
        System.out.println("Факториал числа " + num + " равен " + fact + "\n\n");
        scanner.close();
    }
    public static BigInteger calcFact(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Нету факториала для отрицательных чисел");
        }
        BigInteger fact = BigInteger.valueOf(1);
        for (int i = 1; i <= n; i++) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }
}
