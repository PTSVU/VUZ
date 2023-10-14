package vuz.java.pract2;


import vuz.java.pract1.Base;

import java.util.Scanner;

public class Pract2 extends Base {
    public Pract2() {
        super(0);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pract2 Pract2 = new Pract2();
        System.out.println("""
                Выбирайте задание:
                \t0 = все задания
                \t1 = задание №1
                \t2 = задание №2
                \t3 = задание №3
                \t4 = задание №4
                \t5 = задание №5
                \t6 = задание №6
                \t7 = задание №7
                \t8 = задание №8
                \t9 = задание №9
                \t10 = задание №10""");
        String var = scanner.nextLine();
        System.out.println("\n");
        switch (var) {
            case "0" -> {
                System.out.println("1");          // задание №1
                System.out.println("2");          // задание №2
                System.out.println("3");          // задание №3
                System.out.println("4");          // задание №4
                System.out.println("5");          // задание №5
                System.out.println("6");          // задание №6
                System.out.println("7");          // задание №7
                System.out.println("8");          // задание №8
                System.out.println("9");          // задание №9
                System.out.println("10");          // задание №10
            }
            case "1" -> System.out.println("1");  // задание №1
            case "2" -> System.out.println("2");  // задание №2
            case "3" -> System.out.println("3");  // задание №3
            case "4" -> System.out.println("4");  // задание №4
            case "5" -> System.out.println("5");  // задание №5
            case "6" -> System.out.println("6");  // задание №6
            case "7" -> System.out.println("7");  // задание №7
            case "8" -> System.out.println("8");  // задание №8
            case "9" -> System.out.println("9");  // задание №9
            case "10" -> System.out.println("10");  // задание №10
            default -> System.out.println("Такого задания в практике 2 нету");
        }
    }
}
