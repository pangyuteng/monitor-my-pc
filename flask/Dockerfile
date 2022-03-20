FROM tensorflow/tensorflow:2.6.0-gpu-jupyter

RUN apt-get update && \
    apt-get install lm-sensors sysstat curl wget vim -yq;

COPY requirements.txt /opt

WORKDIR /opt
RUN pip install -r requirements.txt

COPY . /opt
