FROM python:2.7.12
MAINTAINER Tweet Service <patyogesh@gmail.com, bhavnesh.gugnani@gmail.com>
RUN pip install kafka-python
RUN mkdir /usr/bin/TweetService
COPY src/TweetConsumer.py /usr/bin/TweetService
