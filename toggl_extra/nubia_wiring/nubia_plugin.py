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

import argparse
from toggl_extra.nubia_wiring import nubia_commands
from toggl_extra.nubia_wiring.nubia_context import NubiaTogglExtraContext
from toggl_extra.nubia_wiring.nubia_statusbar import NubiaTogglExtraStatusBar
from nubia import PluginInterface, CompletionDataSource
from nubia.internal.blackcmd import CommandBlacklist
from nubia.internal.cmdbase import AutoCommand


class NubiaTogglExtraPlugin(PluginInterface):
    """
    The PluginInterface class is a way to customize nubia_wiring for every customer
    use case. It allows custom argument validation, control over command
    loading, custom context objects, and much more.
    """

    def create_context(self):
        """
        Must create an object that inherits from `Context` parent class.
        The plugin can return a custom context but it has to inherit from the
        correct parent class.
        """
        return NubiaTogglExtraContext()

    def validate_args(self, args):
        """
        This will be executed when starting nubia_wiring, the args passed is a
        dict-like object that contains the argparse result after parsing the
        command line arguments. The plugin can choose to update the context
        with the values, and/or decide to raise `ArgsValidationError` with
        the error message.
        """
        pass

    def get_commands(self):
        return [
            AutoCommand(nubia_commands.dump_entries),
        ]

    def get_opts_parser(self, add_help=True):
        """
        Builds the ArgumentParser that will be passed to , use this to
        build your list of arguments that you want for your shell.
        """
        opts_parser = argparse.ArgumentParser(
            description="Nubia Toggl Extra Utility",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=add_help,
        )
        opts_parser.add_argument(
            "--config", "-c", default="", type=str, help="Configuration File"
        )
        opts_parser.add_argument(
            "--verbose",
            "-v",
            action="count",
            default=0,
            help="Increase verbosity, can be specified " "multiple times",
        )
        opts_parser.add_argument(
            "--stderr",
            "-s",
            action="store_true",
            help="By default the logging output goes to a "
            "temporary file. This disables this feature "
            "by sending the logging output to stderr",
        )
        return opts_parser

    def get_completion_datasource_for_global_argument(self, argument):
        if argument == "--config":
            return ConfigFileCompletionDataSource()
        return None

    def create_usage_logger(self, context):
        """
        Override this and return you own usage logger.
        Must be a subtype of UsageLoggerInterface.
        """
        return None

    def get_status_bar(self, context):
        """
        This returns the StatusBar object that handles the bottom status bar
        and the right-side per-line status
        """
        return NubiaTogglExtraStatusBar(context)

    def getBlacklistPlugin(self):
        black_lister = CommandBlacklist()
        black_lister.add_blocked_command("be-blocked")
        return black_lister


class ConfigFileCompletionDataSource(CompletionDataSource):
    def get_all(self):
        return ["/tmp/c1", "/tmp/c2"]
