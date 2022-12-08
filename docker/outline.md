## setup:

python3 -m venv <directory_name>
source <directory_name>/bin/activate

## Setup

pip3 install Flask
pip3 freeze | grep Flask >> requirements.txt


## App

app.py 

```
 from flask import Flask
 app = Flask(__name__)

 @app.route('/')
 def hello_world():
     return 'Hello, Docker!'
```

## Run

python3 -m flask run --host=0.0.0.0 --port=5000


## Docker file

```
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
```

