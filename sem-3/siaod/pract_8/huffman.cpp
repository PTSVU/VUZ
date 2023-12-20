#include "huffman.h"

#include <iostream>
#include <map>

void counter(std::map<char, int>& res, std::string s) {
    for (int i = 0; i < s.length(); i++) {
        if (res.count(s[i]) == 0) {
            res[s[i]] = 0;
        }
        res[s[i]]++;
    }
}

void create_hoffman_table(Node* node, std::map<char, std::string>& table, std::string code) {
    if (node->label != "") {
        table[node->label.at(0)] = code;
    }
    if (node->left != nullptr) {
        create_hoffman_table(node->left, table, code + "0");
    }
    if (node->right != nullptr) {
        create_hoffman_table(node->right, table, code + "1");
    }
}

void encode_haffman(std::string str) {
	std::map<char, int> alf;
    counter(alf, str);

	std::vector<Node*> queue;

    for (auto symbol : alf) {
        Node* node = new Node();
        node->label = symbol.first;
        node->val = symbol.second;
        queue.push_back(node);
    }

    sort(queue.begin(), queue.end(), [](const Node* a, const Node* b) {
        return a->val < b->val;
        });

    while (queue.size() >= 2) {
        Node* first = queue[0];
        Node* second = queue[1];
        queue.erase(queue.begin());
        queue.erase(queue.begin());

        Node* new_node = new Node();
        new_node->val = first->val + second->val;
        new_node->label = "";
        new_node->left = first;
        new_node->right = second;
        queue.push_back(new_node);
        sort(queue.begin(), queue.end(), [](const Node* a, const Node* b) {
            return a->val < b->val;
            });
    }

    Node* hoffman_tree = queue[0];

	std::map<char, std::string> code_table;
    create_hoffman_table(hoffman_tree, code_table);

	std::string code = "";
    int code_len = 0;
    for (int i = 0; i < str.length(); i++) {
        code += code_table[str.at(i)];
        code_len += code_table[str.at(i)].length();
    }
	std::cout << "Незакодированная строка: " << str << ", размер = " << str.length() << '\n';
	std::cout << "Закодированная фраза: " << code << ", размер = " << code_len << '\n';
	std::cout << "Эффективность сжатия: " << (1 - (code_len / ((double)str.length() * 8))) * 100 << '%';
}