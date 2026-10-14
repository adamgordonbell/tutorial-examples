hhttps://earthly.dev/blog/python-makefile/
# Intro
Hey, in this video I'm going to show you how and why to use makefiles with python.
How to setup virtual environments and develop faster using this old fashioned tool
And if you stay to the end, I'll share why makefiles are still a great choice for a modern developer

# Code Review

* here is my code, it pulls from http://numbersapi.com/, it has requirements.txt.

To run it, I first need to grab its deps
pip install -r requirements.txt

Then I can run it like this:
python -m venv venv4


Afterwards, I can remove the temp code with:
rm -rf __pycache__
(Python is an interpretted language, but It's complicated)

Let make this into a make file:
  makefile.first 
  explain setup, run, clean, phony and default
  touching requirements

To run it 
Run: python app.py


Ok, let's make this into a makefile, so I don't have to do this all the time.

Now lets use venv, so our python program is isolated from others.

python -m venv venv
chmod +x venv/bin/activate
source ./venv/bin/activate
pip install -r requirements.txt
python app.py

Now make file:
create install
use ONESHELL
try it:
make 

make vs gmake

# Why
* works with any languages
* worked with many tools
* you can customize it, do whatever you want. 
  You can add targets for any little thing you want to do.
  Popular in golang community for whatever reason

# Outro

If you looking to learn more about building software, subscribe to the channel. If you want to learn more about Earthly, which is like a make file brought into the future got to earthly.dev or check the link in the description. 

I work for Earthly and it's a great way to build things. It's sort of like docker for builds. Works locally and works with your existing CI.
