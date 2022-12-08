Hey, today we're going to see how to put python apps in docker continers.

It's super easy, and I'll give you a great debugging tip, for what to do when you get into trouble. 

Let's start.



## setup:

python3 -m venv .
chmod +x ./bin/activate
./bin/activate  

## Setup

pip3 install Flask
pip3 freeze | grep Flask >> requirements.txt

## Run

1) python3 -m flask run --host=0.0.0.0 --port=5000

## Docker

2) docker build --tag dockerpy .
3) docker images | grep "dockerpy"

# Earthly

4) earthly --interactive +build








That was dockerizing python. 

IF there are other things you'd like to see then let me know.

And checkout earthly. 

IT does a lot else, and will make your life easy. 

The link in the video description.


