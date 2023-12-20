#include <iostream>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <cstdlib>

#ifdef _WIN32
#include <windows.h>
#elif __linux__
#include <unistd.h>
#elif __APPLE__
#include <unistd.h>
#endif

struct Node {
    int value;
    std::unordered_map<int, int> edges;

    Node(int val) : value(val) {}
};

class Graph {
private:
    std::vector<Node> nodes;

public:
    void addNode(int value) {
        nodes.emplace_back(value);
    }

    void addEdge(int from, int to, int weight) {
        if (from > nodes.size()) {
            addNode(from);
        }
        if (to > nodes.size()) {
            addNode(to);
        }

        nodes[from - 1].edges[to] = weight;
    }

    void printGraph() const {
        for (const auto& node : nodes) {
            std::cout << "Узел " << node.value << ": ";
            for (const auto& edge : node.edges) {
                std::cout << "(" << edge.first << ", " << edge.second << ") ";
            }
            std::cout << std::endl;
        }
    }

    void generateDOT(const std::string& filename) const {
        std::ofstream dotFile(filename);
        if (!dotFile.is_open()) {
            std::cerr << "Не удалось открыть файл для записи." << std::endl;
            return;
        }

        dotFile << "digraph G {\n" << "\tnode[shape = circle]\n" << "\tedge[fontsize = 10]\n";
        for (const auto& node : nodes) {
            for (const auto& edge : node.edges) {
                dotFile << "\t" << node.value << " -> " << edge.first << " [label=" << edge.second << "];\n";
            }
        }
        dotFile << "}\n";

        std::cout << "DOT код сгенерирован в файле '" << filename << "'" << std::endl;
    }

    void renderGraph(const std::string& dotFilename, const std::string& outputFilename) const {
        std::string command = "dot -Tpng " + dotFilename + " -o " + outputFilename;
        system(command.c_str());
        std::cout << "Граф отрендерен в файл '" << outputFilename << "'" << std::endl;
    }

    void openFile(const std::string& filename) const {
#ifdef _WIN32
        ShellExecuteA(nullptr, "open", filename.c_str(), nullptr, nullptr, SW_SHOWNORMAL);
#elif __linux__
        execl("/usr/bin/xdg-open", "xdg-open", filename.c_str(), nullptr);
#elif __APPLE__
        execl("/usr/bin/open", "open", filename.c_str(), nullptr);
#endif
    }

    void floydWarshall() {
        int numNodes = nodes.size();
        std::vector<std::vector<int>> dist(numNodes, std::vector<int>(numNodes, INT_MAX));

        for (int i = 0; i < numNodes; ++i) {
            dist[i][i] = 0;
            for (const auto& edge : nodes[i].edges) {
                dist[i][edge.first - 1] = edge.second;
            }
        }

        for (int k = 0; k < numNodes; ++k) {
            for (int i = 0; i < numNodes; ++i) {
                for (int j = 0; j < numNodes; ++j) {
                    if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX && dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        std::cout << "\nМатрица кратчайших путей:\n\n";
        std::cout << "      ";
        for (int i = 0; i < numNodes; ++i) {
            std::cout << "| " << nodes[i].value << " ";
        }
        std::cout << "\n--------------------------------\n";

        for (int i = 0; i < numNodes; ++i) {
            // Вывод заголовка строки
            std::cout << " " << nodes[i].value << "   | ";
            for (int j = 0; j < numNodes; ++j) {
                if (dist[i][j] == INT_MAX) {
                    std::cout << "?   ";
                }
                else {
                    std::cout << dist[i][j] << "   ";
                }
            }
            std::cout << "\n";
        }
    }
};

int main() {
    setlocale(LC_ALL, "Russian");
    Graph graph;

    int choice;

    std::cout << "Вариант 1: Предустановленный граф\n" << std::endl;
    std::cout << "Вариант 2: Ручной ввод\n" << std::endl;
    std::cout << "Выберите вариант (1 или 2): ";
    std::cin >> choice;

    if (choice == 1) {
        // Вариант 1: Предустановленный граф
        graph.addEdge(1, 2, 8);
        graph.addEdge(1, 3, 4);
        graph.addEdge(2, 4, 6);
        graph.addEdge(2, 5, 3);
        graph.addEdge(3, 4, 2);
        graph.addEdge(3, 5, 1);
        graph.addEdge(3, 6, 10);
        graph.addEdge(4, 5, 3);
        graph.addEdge(4, 6, 1);
        graph.addEdge(5, 6, 4);
        graph.printGraph();
        const std::string dotFilename1 = "graph.dot";
        const std::string outputFilename1 = "graph.png";
        graph.generateDOT(dotFilename1);
        graph.renderGraph(dotFilename1, outputFilename1);
        graph.openFile(outputFilename1);
    }
    else if (choice == 2) {
        // Вариант 2: Ручной ввод
        int numNodes, numEdges;
        std::cout << "Введите количество узлов: ";
        std::cin >> numNodes;

        for (int i = 1; i <= numNodes; ++i) {
            graph.addNode(i);
        }

        std::cout << "Введите количество рёбер: ";
        std::cin >> numEdges;

        for (int i = 0; i < numEdges; ++i) {
            int from, to, weight;
            std::cout << "Введите ребро " << i + 1 << " (от куда, куда, вес): ";
            std::cin >> from >> to >> weight;
            graph.addEdge(from, to, weight);
        }

        graph.printGraph();
        const std::string dotFilename2 = "graph.dot";
        const std::string outputFilename2 = "graph.png";
        graph.generateDOT(dotFilename2);
        graph.renderGraph(dotFilename2, outputFilename2);
        graph.openFile(outputFilename2);
    }
    else {
        std::cout << "Неверный выбор. Программа завершается." << std::endl;
        return 1;
    }

    // Нахождение кратчайших путей методом Флойда
    graph.floydWarshall();

    return 0;
}
