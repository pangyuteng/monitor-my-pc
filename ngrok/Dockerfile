FROM ubuntu:18.04

RUN apt-get update && apt-get install wget vim -yq;

WORKDIR /opt
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz

RUN tar xvzf ngrok-stable-linux-amd64.tgz -C /usr/local/bin
