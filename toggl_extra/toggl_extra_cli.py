#!/usr/bin/env python
import os
import sys

from nubia import Nubia
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from toggl_extra.nubia_wiring.nubia_plugin import NubiaTogglExtraPlugin


if __name__ == '__main__':
    plugin = NubiaTogglExtraPlugin()
    shell = Nubia(name="toggl_extra_cli", plugin=plugin)
    sys.exit(shell.run())
