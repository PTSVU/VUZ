#include "AVLTree.h"
#include <iostream>
#include <iomanip>

AVLNode::AVLNode(double val) : value(val), left(nullptr), right(nullptr), height(1) {}

AVLTree::AVLTree() : root(nullptr) {}

int AVLTree::getHeight(AVLNode* node) {
    return (node != nullptr) ? node->height : 0;
}

int AVLTree::getBalanceFactor(AVLNode* node) {
    return (node != nullptr) ? getHeight(node->left) - getHeight(node->right) : 0;
}

void AVLTree::updateHeight(AVLNode* node) {
    if (node != nullptr) {
        node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
    }
}

AVLNode* AVLTree::rotateRight(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;

    x->right = y;
    y->left = T2;

    updateHeight(y);
    updateHeight(x);

    return x;
}

AVLNode* AVLTree::rotateLeft(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;

    y->left = x;
    x->right = T2;

    updateHeight(x);
    updateHeight(y);

    return y;
}

AVLNode* AVLTree::balance(AVLNode* node) {
    if (node == nullptr) {
        return nullptr;
    }

    updateHeight(node);

    int balance = getBalanceFactor(node);

    if (balance > 1) {
        if (getBalanceFactor(node->left) < 0) {
            node->left = rotateLeft(node->left);
        }
        return rotateRight(node);
    }

    if (balance < -1) {
        if (getBalanceFactor(node->right) > 0) {
            node->right = rotateRight(node->right);
        }
        return rotateLeft(node);
    }

    return node;
}

AVLNode* AVLTree::insert(AVLNode* node, double value) {
    if (node == nullptr) {
        return new AVLNode(value);
    }

    if (value < node->value) {
        node->left = insert(node->left, value);
    }
    else if (value > node->value) {
        node->right = insert(node->right, value);
    }
    else {
        return node;
    }

    return balance(node);
}

void AVLTree::reverseInOrderTraversal(AVLNode* node) {
    if (node != nullptr) {
        reverseInOrderTraversal(node->right);
        std::cout << std::fixed << std::setprecision(2) << node->value << " ";
        reverseInOrderTraversal(node->left);
    }
}

void AVLTree::inOrderTraversal(AVLNode* node) {
    if (node != nullptr) {
        inOrderTraversal(node->left);
        std::cout << std::fixed << std::setprecision(2) << node->value << " ";
        inOrderTraversal(node->right);
    }
}

double AVLTree::sumLeafValues(AVLNode* node, double& sum, int& count) {
    if (node != nullptr) {
        if (node->left == nullptr && node->right == nullptr) {
            sum += node->value;
            count++;
        }
        sumLeafValues(node->left, sum, count);
        sumLeafValues(node->right, sum, count);
    }
    return sum;
}

double AVLTree::calculateAverage(AVLNode* node, double& sum, int& count) {
    sumLeafValues(node, sum, count);
    return (count != 0) ? (sum / count) : 0;
}

void AVLTree::insert(double value) {
    root = insert(root, value);
}

void AVLTree::reverseInOrderTraversal() {
    std::cout << "Обратный обход: ";
    reverseInOrderTraversal(root);
    std::cout << std::endl;
}

void AVLTree::inOrderTraversal() {
    std::cout << "Симметричный обход: ";
    inOrderTraversal(root);
    std::cout << std::endl;
}

double AVLTree::sumLeafValues() {
    double sum = 0.0;
    int count = 0;
    return sumLeafValues(root, sum, count);
}

double AVLTree::calculateAverage() {
    double sum = 0.0;
    int count = 0;
    return calculateAverage(root, sum, count);
}

void AVLTree::displayMenu() {
    std::cout << "Меню AVL-дерева:" << std::endl;
    std::cout << "1. Вставить элемент" << std::endl;
    std::cout << "2. Обратный обход" << std::endl;
    std::cout << "3. Симметричный обход" << std::endl;
    std::cout << "4. Сумма значений листьев" << std::endl;
    std::cout << "5. Среднее значение всех узлов" << std::endl;
    std::cout << "0. Выход" << std::endl;
    std::cout << "Введите ваш выбор: ";
}

void AVLTree::processAction(int choice) {
    switch (choice) {
    case 1: {
        double value;
        std::cout << "Введите значение для вставки: ";
        std::cin >> value;
        insert(value);
        break;
    }
    case 2:
        reverseInOrderTraversal();
        break;
    case 3:
        inOrderTraversal();
        break;
    case 4:
        std::cout << "Сумма значений листьев: " << sumLeafValues() << std::endl;
        break;
    case 5:
        std::cout << "Среднее значение всех узлов: " << calculateAverage() << std::endl;
        break;
    case 0:
        std::cout << "Выход из программы." << std::endl;
        break;
    default:
        std::cout << "Неверный выбор. Пожалуйста, введите число от 0 до 5." << std::endl;
    }
}