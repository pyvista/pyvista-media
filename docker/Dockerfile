FROM ubuntu:22.10
MAINTAINER tkoyama010@gmail.com

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
ENV TERM xterm
ENV TAG_NAME=master

USER root
WORKDIR work

# install dependencies

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl
RUN apt-get install -y --no-install-recommends firefox
RUN apt-get install -y --no-install-recommends python-is-python3
RUN apt-get install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends python3-venv
RUN apt-get install -y --no-install-recommends xterm

# compile and install

RUN python3 -m venv /venv
RUN source /venv/bin/activate && \
    pip install --no-cache --upgrade pip && \
    pip install mkposters==0.0.4 && \
    deactivate

