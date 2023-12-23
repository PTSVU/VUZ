#include <iostream>
#include <cstring>

typedef struct tag_data {
    char name[100];
} DATA;

typedef struct tag_tree {
    DATA data;
    struct tag_tree* left, * right;
} TREE;

enum TYPE { RIGHT, LEFT };

TREE* add_node(TREE* node, const char* name, TYPE type = LEFT) {
    TREE* new_node = new TREE;
    if (type == LEFT && node != NULL)
        node->left = new_node;
    else if (node != NULL)
        node->right = new_node;

    strcpy_s(new_node->data.name, sizeof(new_node->data.name), name);

    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

void copy_left_to_right(TREE* node) {
    if (node != NULL) {
        if (node->left != NULL) {
            if (node->right != NULL)
				strcpy_s(node->right->data.name, sizeof(node->right->data.name), node->left->data.name);

            copy_left_to_right(node->left);
            copy_left_to_right(node->right);
        }
    }
}

void show_next(TREE* node, int off) {
    if (node != NULL) {
        for (int i = 0; i < off; i++)
            putchar(' ');
        printf("%s\n", node->data.name);
        show_next(node->left, off);
        show_next(node->right, off + 1);
    }
}

void show_tree(TREE* root) {
    if (root != NULL) {
        printf("%s\n", root->data.name);
        show_next(root->left, 0);
        show_next(root->right, 1);
    }
}

void del_next(TREE* node) {
    if (node != NULL) {
        del_next(node->left);
        del_next(node->right);
        printf("node %s - deleted\n", node->data.name);
        delete node;
    }
}

void del_tree(TREE* root) {
    if (root != NULL) {
        del_next(root->left);
        del_next(root->right);
        printf("node %s - deleted\n", root->data.name);
        delete root;
    }
}

int main() {
    TREE* root = add_node(NULL, "Root");
    TREE* current = add_node(root, "File 1", LEFT);
    current = add_node(current, "File 2", LEFT);
    current = add_node(root, "Folder 1", RIGHT);
    current = add_node(current, "File 11", LEFT);
    current = add_node(current, "File 12", LEFT);
    current = add_node(root->right, "Folder 2", RIGHT);
    current = add_node(current, "File 21", RIGHT);

    std::cout << "Original Tree:" << std::endl;
    show_tree(root);

    // Копирование вершин с левого указателя в правый
    copy_left_to_right(root);

    std::cout << "\nTree After Copying Left to Right:" << std::endl;
    show_tree(root);

    del_tree(root); // Освобождение памяти

    return 0;
}
