all: hello

hello: main.o hello.o
    g++ main.o hello.o -o hello
    echo "Executable file 'hello' has been created."

main.o: main.cpp main.h
    g++ -c main.cpp
    echo "Compiled main.cpp."

hello.o: hello.cpp main.h
    g++ -c hello.cpp
    echo "Compiled hello.cpp."
