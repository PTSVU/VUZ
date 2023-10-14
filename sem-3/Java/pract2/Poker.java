package vuz.java.pract2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Poker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите количество игроков: ");
        int numPlayers = scanner.nextInt();

        if (numPlayers < 1 || numPlayers > 10) {
            System.out.println("Количество игроков должно быть от 1 до 10.");
            return;
        }

        List<String> deck = initializeDeck();
        shuffleDeck(deck);

        int numCardsPerPlayer = 5;
        for (int i = 0; i < numPlayers; i++) {
            List<String> hand = dealHand(deck, numCardsPerPlayer);
            System.out.println("Игрок " + (i + 1) + " получил карты:");
            printHand(hand);
            System.out.println();
        }

        scanner.close();
    }

    private static List<String> initializeDeck() {
        List<String> deck = new ArrayList<>();
        String[] suits = { "Черви", "Бубны", "Крести", "Пики" };
        String[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз" };

        for (String suit : suits) {
            for (String rank : ranks) {
                deck.add(rank + " " + suit);
            }
        }

        return deck;
    }

    private static void shuffleDeck(List<String> deck) {
        Collections.shuffle(deck);
    }

    private static List<String> dealHand(List<String> deck, int numCards) {
        List<String> hand = new ArrayList<>();
        for (int i = 0; i < numCards; i++) {
            hand.add(deck.remove(0)); // Убираем верхнюю карту из колоды и добавляем ее в руку
        }
        return hand;
    }

    private static void printHand(List<String> hand) {
        for (String card : hand) {
            System.out.println(card);
        }
    }
}
