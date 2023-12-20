#include <iostream>
#include <vector>
#include <iomanip>

int min(int a, int b, int c) {
    return std::min(std::min(a, b), c);
}

void printField(const std::vector<std::vector<int>>& field, const std::vector<std::vector<bool>>& shortestPath) {
    std::cout << "Поле:\n";
    for (int i = 0; i < field.size(); ++i) {
        for (int j = 0; j < field[i].size(); ++j) {
            if (shortestPath[i][j]) {
                std::cout << std::setw(3) << field[i][j] << " ";
            }
            else {
                std::cout << "   ";
            }
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

void printOriginalField(const std::vector<std::vector<int>>& field) {
    std::cout << "Изначальное поле:\n";
    for (const auto& row : field) {
        for (int value : row) {
            std::cout << std::setw(3) << value << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main() {
    setlocale(LC_ALL, "Russian");
    int choice;
    std::cout << "Выберите вариант:\n";
    std::cout << "1. Предустановленное поле\n";
    std::cout << "2. Ручной ввод поля\n";
    std::cin >> choice;

    int n, m;
    std::vector<std::vector<int>> field;

    if (choice == 1) {
        // Предустановленное поле
        n = 3;
        m = 4;
        field = { {1, 2, 3, 4},
                 {5, 6, 7, 8},
                 {9, 10, 11, 12} };
    }
    else if (choice == 2) {
        // Ручной ввод поля
        std::cout << "Введите размеры поля n и m: ";
        std::cin >> n >> m;

        std::cout << "Введите значения клеток поля:\n";
        field.resize(n, std::vector<int>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                std::cin >> field[i][j];
            }
        }
    }
    else {
        std::cout << "Неверный выбор. Программа завершается.\n";
        return 1;
    }

    printOriginalField(field);

    std::vector<std::vector<int>> dp(n, std::vector<int>(m));

    // Инициализация значений в массиве dp
    dp[0][0] = field[0][0];
    for (int i = 1; i < n; ++i) {
        dp[i][0] = dp[i - 1][0] + field[i][0];
    }
    for (int j = 1; j < m; ++j) {
        dp[0][j] = dp[0][j - 1] + field[0][j];
    }

    // Заполнение массива dp
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < m; ++j) {
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + field[i][j];
        }
    }

    // Восстановление маршрута
    std::cout << "Минимальный вес маршрута: " << dp[n - 1][m - 1] << std::endl;

    // Восстановление маршрута
    std::vector<std::vector<bool>> shortestPath(n, std::vector<bool>(m, false));
    int i = n - 1, j = m - 1;
    while (i > 0 || j > 0) {
        shortestPath[i][j] = true;
        if (i > 0 && j > 0) {
            int min_neighbour = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
            if (min_neighbour == dp[i - 1][j - 1]) {
                --i;
                --j;
            }
            else if (min_neighbour == dp[i - 1][j]) {
                --i;
            }
            else {
                --j;
            }
        }
        else if (i > 0) {
            --i;
        }
        else {
            --j;
        }
    }
    shortestPath[0][0] = true;

    printField(field, shortestPath);

    return 0;
}
