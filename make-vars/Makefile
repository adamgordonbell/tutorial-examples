.DEFAULT_GOAL := run

main.o: src/main.c 
	gcc -o target/hello src/main.c

run: main.o
	./target/hello

clean:
	rm -rf target/hello
	rm combined.md

.phony: clean run test

# foo1 = World

# foo2 = one$two

# foo3 = one$$two


# test1: 
# 	@echo "foo1=$(foo1)"
# 	@echo "foo2=$(foo2)"
# 	@echo "foo3=$(foo3)"
# # how to use variables in a string
# 	@echo "Hello, $(foo1)!"
# # What if no variable is defined?
# 	@echo "Hello, $(foo)!"

# # Using a list of vars
# objects = text/one.md text/two.md text/three.md
# combined.md : $(objects) 
# 	cat $(objects) > combined.md

# $(objects) : src/main.c

# # Things get complicated

# #######################
# # Recursive assignment
# #######################

# #  foobar, foo, bar, baz, qux, quux, corge, grault, garply, waldo, fred, plugh, xyzzy

# bar = Hello $(baz)
# baz = World

# quux = $(baz)
# qux = Hello $(quux)
# quux = Make

# corge = start
# corge = $(corge) and add more

# test2:
# 	@echo "bar=$(bar)"
# 	@echo "qux=$(qux)"
# 	@echo "corge=$(corge)"
		
# #####################
# # Simple assignment
# #####################

# bar1 := Hello $(baz1)
# baz1 := World

# quux1 := $(baz1)
# qux1 := Hello $(quux1)
# quux1 := Make

# corge1 := start
# corge1 := $(corge1) and add more

# test3:
# 	@echo "bar1=$(bar1)"
# 	@echo "qux1=$(qux1)"
# 	@echo "corge1=$(corge1)"

# #####################
# # Better Appending
# #####################
# foo4 = Hello
# foo4 += World

# bar4 := Hello
# bar4 += World

# # Both print "Hello World"
# test4:
# 	@echo ${foo4}
# 	@echo ${bar4}

# # How does uncommenting this change the output of test4?
# foo4 = more
# bar4 := more

# #########################
# # Conditional assignment
# #########################

# foo5 = World

# foo5 ?= Make # foo will not change
# bar5 ?= Make # bar will change

# test5:
# 	@echo Hello ${foo5}
# 	@echo Hello ${bar5}

# ########################
# # Target Specific Vars 
# #########################
# foo6 = Hello

# test6a: foo6 = Sup
# test6b: foo6 = Hey


# test6:
# 	@echo "$(foo6)!"

# test6a: test6
# 	@echo "test6a"

# test6b: test6
# 	@echo "test6b"

# #######################
# # The environment  
# #######################

# # override me x=y
# foo7 = Hello
# bar7 = World

# test7:
# 	@echo ${USER}
# 	@echo ${foo7} ${bar7}

# #######################
# ## Magic Variables    #
# #######################

# prereq1:
# 	@echo "prereq1"

# prereq2:
# 	@echo "prereq2"

# test8: prereq1 prereq2
# 	@echo "\n\nMagic Variables:"
# 	@echo "Target:			$@"
# 	@echo "First Prereq:		$< "
# 	@echo "Changed PreReq:		$?"
# 	@echo "All PreReqs:		$^"
