#!/usr/bin/env python3

from argparse import ArgumentParser
from soundify import soundify

__author__ = '@amiremohamadi'
__version__ = '0.1'
__description__ = f'to soundify error codes. version {__version__}'


def main():
    '''
    parse args and start the script
    '''

    parser = ArgumentParser(description=__description__)
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('command', nargs='+', help='command to run')
    args = parser.parse_args()

    print(args.command)

    return soundify(args.command)


if __name__ == '__main__':
    ret = main()
    # exit with that command exitcode
    exit(ret)
