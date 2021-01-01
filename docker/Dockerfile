# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# Instructions:
# docker build -f docker/Dockerfile --build-arg UID=$(id -u) --build-arg GID=$(id -g) --target builder -t logdevice_build .
# docker run -it -v $(pwd):/home/ubuntu/LogDevice logdevice_build

FROM ubuntu:bionic as builder

MAINTAINER Ahmed Soliman <asoli@fb.com>

ARG UID=1000
ARG GID=1000
# Controls the build parallelism, it defaults to the number of cores, use this
# to reduce the total memory used during compilation.
ARG PARALLEL

# Running tests as root would miss permissions issues, so create a non-root
# user

COPY logdevice/build_tools/ubuntu.deps /tmp/ubuntu.deps

RUN apt-get update \
    && apt-get install --no-install-recommends \
      -y $(cat /tmp/ubuntu.deps) \
         python3-virtualenv \
         python3-setuptools \
         sudo \
    && rm -rf /var/lib/apt/lists/* 

RUN groupadd -g ${GID} ubuntu \
    && useradd -ms /bin/bash -N -u ${UID} -g ${GID} ubuntu
RUN echo "ubuntu ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ubuntu

USER ubuntu
RUN mkdir -p /home/ubuntu/_build/staging/usr/local
WORKDIR /home/ubuntu/_build
ENV LANG C.UTF-8

ENV VIRTUAL_ENV=/home/ubuntu/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install --upgrade setuptools wheel cython

RUN echo 'echo cmake -Dthriftpy3=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF ${HOME}/LogDevice/logdevice/' >> ${HOME}/.bashrc

ENV CC=clang-9
ENV CXX=clang++-9

CMD /bin/bash
