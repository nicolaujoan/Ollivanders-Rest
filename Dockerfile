FROM python:3.9-slim-bullseye

RUN apt-get update -y

EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT flask run --host=0.0.0.0 --port=5000
