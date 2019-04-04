#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from shell_quoting import ShellQuoted

def fbcode_builder_spec(builder):
    # FIXME: Assert job must have venv enabled for this to work
    return {
        "steps": [
            builder.step(
                "Install Cython from pip",
                [builder.run(ShellQuoted("pip install cython"))],
            ),
        ],
    }
