#
# A simple makefile for compiling a c++ project
#

all: clean default test

default: CoinFlipper.cpp

CoinFlipper.cpp: 
	gcc -o ./target/CoinFlipper.out ./src/main/CoinFlipper.cpp

run: CoinFlipper.cpp
	./target/CoinFlipper.out 10

test: CoinFlipper.cpp
	./target/CoinFlipper.out 10000

clean: 
	rm -rf ./target/*.out