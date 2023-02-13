#
# A simple makefile for compiling a c++ project
#
.DEFAULT_GOAL := coinflipper.cpp

all: clean test

coinflipper.cpp: 
	gcc -o ./target/coinflipper.out ./src/main/coinflipper.cpp

run: coinflipper.cpp
	./target/coinflipper.out 10

test: coinflipper.cpp
	./target/coinflipper.out 10000

clean: 
	rm -rf ./target/*.out