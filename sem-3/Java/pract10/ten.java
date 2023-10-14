package vuz.java.pract10;

public class ten {

    public static int reverseNumber(int n) {
        return reverseNumber(n, 0);
    }
    public static int reverseNumber(int n, int reversed) {
        if (n == 0) {
            return reversed;
        }
        int digit = n % 10;
        reversed = reversed * 10 + digit;
        return reverseNumber(n / 10, reversed);
    }

    public static void main(String[] args) {
        System.out.println(reverseNumber(256));
    }
}
