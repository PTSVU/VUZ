package vuz.java.pract1;


import java.util.Scanner;

public class Pract1 extends Base {
    public Pract1() {
        super(0);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pract1 Pract1 = new Pract1();
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
                \t8 = задание №8""");
        String var = scanner.nextLine();
        System.out.println("\n");
        switch (var) {
            case "0" -> {
                System.out.println("Создал проэкт");          // задание №1
                System.out.println("Гит создал\n\n");         // задание №2
                ArrSum.main(args);                            // задание №3
                ArrMinMax.main(args);                         // задание №4
                Command.main(args);                           // задание №5
                Harmonic.main(args);                          // задание №6
                Fact.main(args);                              // задание №7
                System.out.println("На гит выложил");         // задание №8
            }
            case "1" -> System.out.println("Создал проэкт");  // задание №1
            case "2" -> System.out.println("Гит создал");     // задание №2
            case "3" -> ArrSum.main(args);                    // задание №3
            case "4" -> ArrMinMax.main(args);                 // задание №4
            case "5" -> Command.main(args);                   // задание №5
            case "6" -> Harmonic.main(args);                  // задание №6
            case "7" -> Fact.main(args);                      // задание №7
            case "8" -> System.out.println("На гит выложил"); // задание №8
            default -> System.out.println("Такого задания в практике 1 нету");
        }
        scanner.close();
    }
}
