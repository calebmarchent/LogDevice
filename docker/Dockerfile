# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

FROM ubuntu:bionic as builder

MAINTAINER Ahmed Soliman <asoli@fb.com>

ARG UID=1000
ARG GID=1000
# Controls the build parallelism, it defaults to the number of cores, use this
# to reduce the total memory used during compilation.
ARG PARALLEL

# Running tests as root would miss permissions issues, so create a non-root
# user
RUN groupadd -g ${GID} ubuntu \
    && useradd -ms /bin/bash -N -u ${UID} -g ${GID} ubuntu

COPY logdevice/build_tools/ubuntu.deps /tmp/ubuntu.deps

RUN apt-get update \
    && apt-get install --no-install-recommends \
      -y $(cat /tmp/ubuntu.deps) \
         python3-virtualenv \
         python3-setuptools \
    && rm -rf /var/lib/apt/lists/* 

USER ubuntu
RUN mkdir -p /home/ubuntu/LogDevice/_build/staging/usr/local
WORKDIR /home/ubuntu/LogDevice/_build
ENV LANG C.UTF-8

ENV VIRTUAL_ENV=/home/ubuntu/LogDevice/_build/staging/usr/local
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install --upgrade setuptools wheel cython

ENV CC=clang-9
ENV CXX=clang++-9

CMD /bin/bash
