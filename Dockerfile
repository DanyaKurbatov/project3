FROM python:3.8-alpine
MAINTAINER project3

ENV venv 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /project3
WORKDIR /project3
COPY ./project3 /project3

RUN adduser -D user
USER user