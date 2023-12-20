#ifndef __SHANNON_FANO_H__
#define __SHANNON_FANO_H__
#include <string>
#include <vector>

struct ShannonFanoNode {
	std::string symbol;
	double probability;
	std::string code;
};

std::vector<ShannonFanoNode> shannonFano(const std::string& data);
#endif