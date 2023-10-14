package vuz.java.pract2;

import java.util.Scanner;

public class HowMany {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите текст: ");

        String input = scanner.nextLine();
        int wordCount = countWords(input);

        System.out.println("Вы ввели " + wordCount + " слов.");

        scanner.close();
    }

    public static int countWords(String text) {
        if (text == null || text.isEmpty()) {
            return 0;
        }

        String[] words = text.split("\\s+"); // Разбиваем текст на слова по пробелам
        return words.length;
    }
}
