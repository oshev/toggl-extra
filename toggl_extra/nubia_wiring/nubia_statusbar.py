#!/usr/bin/env python3

# This class was largely borrowed from
# https://github.com/facebookincubator/python-nubia/tree/master/example
# so the original copyright is kept untouched.
#
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the package.
#

from pygments.token import Token

from nubia import context
from nubia import statusbar


class NubiaTogglExtraStatusBar(statusbar.StatusBar):
    def __init__(self, context):
        self._last_status = None

    def get_rprompt_tokens(self, cli):
        if self._last_status:
            return [(Token.RPrompt, "Error: {}".format(self._last_status))]
        return []

    def set_last_command_status(self, status):
        self._last_status = status

    def get_tokens(self, cli):
        spacer = (Token.Spacer, "  ")
        if context.get_context().verbose:
            is_verbose = (Token.Warn, "ON")
        else:
            is_verbose = (Token.Info, "OFF")
        return [
            (Token.Toolbar, "[Toggl Extra CLI]"),
            spacer,
            (Token.Toolbar, "Verbose "),
            spacer,
            is_verbose,
        ]
