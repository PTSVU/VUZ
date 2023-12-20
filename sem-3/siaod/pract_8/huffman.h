#ifndef __HUFFMAN_H__
#define __HUFFMAN_H__
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>

struct Node {
	std::string label;
    int val;
    Node* left = nullptr;
    Node* right = nullptr;
};

void counter(std::map<char, int>& res, std::string s);
void create_hoffman_table(Node* node, std::map<char, std::string>& table, std::string code = "");
void encode_haffman(std::string str);



#endif