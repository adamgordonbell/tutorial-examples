.DEFAULT_GOAL := run

main.o: src/main.c 
	gcc -o target/hello src/main.c

run: main.o
	./target/hello

clean:
	rm -rf target/hello

.phony: clean run