"""
This file is used for creating .exe file
"""

import os
import importlib

from user.qt_runner import setup_windows


def auto_importer():
    pass


if __name__ == '__main__':
    """ Run the client application. """
    setup_windows()
