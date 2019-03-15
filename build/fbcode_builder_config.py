#!/usr/bin/env python

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import absolute_import, division, print_function, unicode_literals

import specs.rocksdb as rocksdb
import specs.fbthrift as fbthrift
from shell_quoting import ShellQuoted


"fbcode_builder steps to build & test LogDevice"

"""
Running this script from the command line on a dev-server:

1. Ensure you have the HTTP proxy configured in environment
2. This is env items is not compatible with the scutil create call, so must
   not be permenently exported.

git config --global http.proxy http://fwdproxy:8080

cd .../fbcode/logdevice/public_tld/build
HTTP_PROXY=http://fwdproxy:8080 HTTPS_PROXY=http://fwdproxy:8080 \
fbcode/opensource/fbcode_builder/facebook_make_legocastle_job.py \
| scutil create

Which outputs a legocastle job to stdout; to be fed into scutil create ...

"""


def fbcode_builder_spec(builder):
    builder.add_option("LogDevice/logdevice/_build:cmake_defines", {
        "BUILD_SUBMODULES": "OFF",
    })
    return {
        "depends_on": [rocksdb, fbthrift],
        "steps": [
            # This isn"t a separete spec, since only fbthrift uses mstch.
            builder.fb_github_cmake_install("LogDevice/logdevice/_build",
                                            github_org="facebookincubator"),
        ],
    }


config = {
    "github_project": "facebookincubator/LogDevice",
    "fbcode_builder_spec": fbcode_builder_spec,
}
