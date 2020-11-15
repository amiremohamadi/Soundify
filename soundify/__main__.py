from argparse import ArgumentParser
from .soundify import soundify, play
from .config import CONFIG_FILE

__author__ = '@amiremohamadi'
__version__ = '0.4'
__description__ = f'to soundify error codes. version {__version__}'


def test(code):
    '''
    test sounds by exitcode
    '''
    return play(code)


def main():
    '''
    parse args and start the script
    '''

    parser = ArgumentParser(description=__description__)
    parser.add_argument('-v', '--version', action='version', version=__version__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--config-file', action='store_true')
    group.add_argument('-t', '--test', nargs='?', type=int, help='test exitcode sound')
    group.add_argument('command', nargs='?', type=str, help='command to run')
    args = parser.parse_args()

    # show config directory
    if args.config_file:
        print(CONFIG_FILE)
        return 0

    # with --test/-t flag you can test an exitcode sound
    if args.test is not None:
        return test(args.test)

    return soundify(args.command)


if __name__ == '__main__':
    ret = main()
    # exit with that command exitcode
    exit(ret)
