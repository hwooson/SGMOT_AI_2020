FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /source

WORKDIR /source
COPY requirements.txt /source/
RUN pip install -r requirements.txt
