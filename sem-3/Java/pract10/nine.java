package vuz.java.pract10;

public class nine {
    public static int countSequences(int a, int b) {
        int[][] dp = new int[a + 1][b + 1];
        dp[0][0] = 1;

        for (int i = 0; i <= a; i++) {
            for (int j = 0; j <= b; j++) {
                if (i > 0) {
                    dp[i][j] += dp[i - 1][j];
                }
                if (j > 0 && i < 2) {
                    dp[i][j] += dp[i][j - 1];
                }
            }
        }

        return dp[a][b];
    }

    public static void main(String[] args) {
        System.out.println(countSequences(10, 100));
    }

}
