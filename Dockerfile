FROM python:3.5-slim

MAINTAINER Sahand Hariri sahandha@gmail.com

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN apt-get -qq update
RUN apt-get -qq -y install wget curl 
RUN sudo apt-get -qq -y install software-properties-common apt-utils

RUN sudo apt-get install -y python-pip python-dev build-essential
RUN sudo apt-get install -y git
RUN pip install --upgrade pip 

RUN pip install tornado


EXPOSE 8888

Add server.py server.py
Add static static

RUN apt-get install -y vim
