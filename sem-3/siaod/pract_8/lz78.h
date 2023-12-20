#ifndef __LZ78_H__
#define __LZ78_H__
#include <string>
#include <string>
#include <vector>
#include <map>
std::vector<std::pair<int, char>> LZ78Encode(const std::string& data);
std::string LZ78Decode(const std::vector<std::pair<int, char>>& encodedData);
#endif