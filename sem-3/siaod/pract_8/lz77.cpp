#include "lz77.h"
#include <iostream>

std::vector<LZ77Token> LZ77Compress(const std::string& data, int windowSize) {
	std::vector<LZ77Token> compressedData;
	int dataSize = static_cast<int>(data.size());
	int currentIndex = 0;
	while (currentIndex < dataSize) {
		LZ77Token token;
		token.offset = 0;
		token.length = 0;
		token.nextChar = data[currentIndex];
		int searchStart = std::max(currentIndex - windowSize, 0);
		int searchEnd = currentIndex;
		for (int i = searchStart; i < currentIndex; ++i) {
			int currentLength = 0;
			while (currentIndex + currentLength < dataSize && data[i + currentLength] == data[currentIndex + currentLength]) {
				++currentLength;
			}
			if (currentLength > token.length) {
				token.offset = currentIndex - i;
				token.length = currentLength;
				token.nextChar = data[currentIndex + currentLength];
			}
		}
		compressedData.push_back(token);
		currentIndex += token.length + 1;
	}
	return compressedData;
}