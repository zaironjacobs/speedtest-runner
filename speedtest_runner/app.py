import sys
import os
import argparse
import subprocess
import platform
from signal import signal, SIGINT
from pathlib import Path

from . import __version__
from . import arguments

import colorama


def main():
    # noinspection PyUnusedLocal
    def signal_handler(signal_received, frame):
        """ Handles clean Ctrl+C exit """

        sys.stdout.write('\n')
        sys.exit(0)

    signal(SIGINT, signal_handler)
    App()


class App:

    def __init__(self):
        self.__c_fore = colorama.Fore
        self.__c_style = colorama.Style
        colorama.init()

        self.__msg_error_unrecognized_argument = (
                self.__c_fore.RED + 'error: unrecognized argument(s) detected' + self.__c_style.RESET_ALL
                + '\n' + 'tip: use --help to see all available arguments')

        self.__parser = argparse.ArgumentParser(add_help=False)
        for i, arg in enumerate(arguments.args_options):
            self.__parser.add_argument(arguments.args_options[i][0], nargs='*')
        self.__args, self.__unknown = self.__parser.parse_known_args()

        if self.__unknown:
            print(self.__msg_error_unrecognized_argument)
            sys.exit(0)

        ###################
        # DEFAULT NO ARGS #
        ###################
        if len(sys.argv) == 1:
            self.__run()
            sys.exit(0)

        ########
        # HELP #
        ########
        self.__arg_help = self.__args.help
        if self.__arg_passed(self.__arg_help):
            arguments.print_help()
            sys.exit(0)

        ###########
        # VERSION #
        ###########
        self.__arg_version = self.__args.version
        if self.__arg_passed(self.__arg_version):
            print('v' + __version__)
            sys.exit(0)

        #######
        # RUN #
        #######
        self.__arg_run = self.__args.run
        if self.__arg_passed(self.__arg_run):
            self.__run()
            sys.exit(0)

    def __arg_passed(self, arg):
        if isinstance(arg, list):
            return True
        return False

    def __run(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        if platform.system() == 'Windows':
            subprocess.call('speedtest/win/speedtest.exe')
        elif platform.system() == 'Linux':
            file_path = Path('speedtest/linux/speedtest')
            os.chmod(file_path, 0o700)
            subprocess.call('speedtest/linux/speedtest')
        elif platform.system() == 'Darwin':
            subprocess.call('speedtest/mac/speedtest')
