https://earthly.dev/blog/vscode-make/

# Intro
Hey, in this video I'm going to show you how and why to use makefiles in vs code
How to compile, run, test and clean inside vscode.
If you want to get right to the VS code integration, jump about halfway thru
And if you stay to the end, I'll share why makefiles are still a great choice

# Code Review

* Here is code

* Lang doesn't matter, but this will all make sense at make
* build: gcc -o ./target/CoinFlipper.out ./src/main/CoinFlipper.cpp
* run: ./target/CoinFlipper.out 10
* test: ./target/CoinFlipper.out 10000
* clean rm ./target/CoinFlipper.out


# Make file
* explain how these are all the same
* except now they all require build, which is nice
* Caveat: use tabs

# VS code
* install extension "Makefile Tools"
* show how to configure
* show makefile "perspective" or side bar
* show build and run buttons
* show config configuration / build / launch
* show in settings.json

# Why
* works with any languages
* worked with many tools
* you can customize it, do whatever you want. 
  You can add targets for any little thing you want to do.

# Outro

If you looking to learn more about building software, subscribe to the channel. If you want to learn more about Earthly, which is like a make file brought into the future got to earthly.dev or check the link in the description. 

I work for Earthly and it's a great way to build things. It's sort of like docker for builds. Works locally and works with your existing CI.
