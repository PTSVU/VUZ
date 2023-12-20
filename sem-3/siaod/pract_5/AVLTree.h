#ifndef __AVLTREE_H__
#define __AVLTREE_H__
struct AVLNode {
    double value;
    AVLNode* left;
    AVLNode* right;
    int height;

    AVLNode(double val);
};

class AVLTree {
private:
    AVLNode* root;

    int getHeight(AVLNode* node);
    int getBalanceFactor(AVLNode* node);
    void updateHeight(AVLNode* node);
    AVLNode* rotateRight(AVLNode* y);
    AVLNode* rotateLeft(AVLNode* x);
    AVLNode* balance(AVLNode* node);

    AVLNode* insert(AVLNode* node, double value);
    void reverseInOrderTraversal(AVLNode* node);
    void inOrderTraversal(AVLNode* node);
    double sumLeafValues(AVLNode* node, double& sum, int& count);
    double calculateAverage(AVLNode* node, double& sum, int& count);

public:
    AVLTree();

    void insert(double value);
    void reverseInOrderTraversal();
    void inOrderTraversal();
    double sumLeafValues();
    double calculateAverage();
    void displayMenu();
    void processAction(int choice);
};

#endif