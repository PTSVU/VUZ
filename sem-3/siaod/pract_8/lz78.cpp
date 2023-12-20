#include "lz78.h"
#include <iostream>

std::vector<std::pair<int, char>> LZ78Encode(const std::string& data) {
	std::vector<std::pair<int, char>> encodedData;
	std::map<std::string, int> dictionary;
	int currentIndex = 0;
	for (char c : data) {
		std::string currentPhrase = std::string(1, c);
		if (dictionary.count(currentPhrase) > 0) {
			currentIndex = dictionary[currentPhrase];
		}
		else {
			encodedData.emplace_back(currentIndex, c);
			dictionary[currentPhrase] = currentIndex + 1;
			currentIndex++;
		}
	}
	return encodedData;
}

std::string LZ78Decode(const std::vector<std::pair<int, char>>& encodedData) {
	std::string decodedData = "";
	std::map<int, std::string> dictionary;
	for (const auto& pair : encodedData) {
		int index = pair.first; char c = pair.second;
		std::string currentPhrase;
		if (dictionary.count(index) > 0) {
			currentPhrase = dictionary[index];
		}
		currentPhrase += c;
		decodedData += currentPhrase;
		dictionary[index + 1] = currentPhrase;
	}
	return decodedData;
}