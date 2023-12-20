#include "AVLTree.h"
#include <iostream>

int main() {
    setlocale(LC_ALL, "Russian");
    AVLTree avlTree;
    int choice;

    do {
        avlTree.displayMenu();
        std::cin >> choice;

        avlTree.processAction(choice);

    } while (choice != 0);

    return 0;
}
