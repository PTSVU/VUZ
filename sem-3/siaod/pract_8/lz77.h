#ifndef __LZ77_H__
#define __LZ77_H__

#include <string>
#include <vector>

struct LZ77Token {
	int offset;
	int length;
	char nextChar;
};
std::vector<LZ77Token> LZ77Compress(const std::string& data, int windowSize);

#endif