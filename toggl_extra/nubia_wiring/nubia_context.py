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
import yaml
from nubia import context
from nubia import exceptions
from nubia import eventbus

CONFIG_PATH = 'configs/toggl-extra.yaml'


class NubiaTogglExtraContext(context.Context):

    def __init__(self):
        super().__init__()
        self.verbose = None
        config_yaml_stream = open(CONFIG_PATH, "r")
        config_root = yaml.load(config_yaml_stream)
        toggl_config_entry = self.get_config_param(config_root, 'Toggl')
        self.toggl_auth_token = self.get_config_param(toggl_config_entry, 'auth_token')

    @staticmethod
    def get_config_param_recursive(entry, elements):
        if len(elements) > 0 and type(entry) is dict:
            return NubiaTogglExtraContext.get_config_param_recursive(entry[elements[0]], elements[1:])
        else:
            return entry

    @staticmethod
    def get_config_param(section_entries, path):
        elements = path.split('.')
        return NubiaTogglExtraContext.get_config_param_recursive(section_entries, elements)

    def on_connected(self, *args, **kwargs):
        pass

    def on_cli(self, cmd, args):
        # dispatch the on connected message
        self.verbose = args.verbose
        self.registry.dispatch_message(eventbus.Message.CONNECTED)

    def on_interactive(self, args):
        self.verbose = args.verbose
        ret = self._registry.find_command("connect").run_cli(args)
        if ret:
            raise exceptions.CommandError("Failed starting interactive mode")
        # dispatch the on connected message
        self.registry.dispatch_message(eventbus.Message.CONNECTED)
