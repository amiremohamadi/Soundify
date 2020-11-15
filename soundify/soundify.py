'''
functions related to main

@authors:
    - @amiremohamadi

changelogs:
    - nothing
'''

from .config import read_config
from subprocess import Popen, DEVNULL
from playsound import playsound, PlaysoundException
from sys import stderr

def play(code):
    '''
    play a sound by exitcode
    '''
    ret = 1
    # a map from error_code to sound_dir
    err_sound = read_config()
    
    sound = err_sound.get(code, None)
    if sound is not None:
        try:
            playsound(sound)
            ret = 0
        except PlaysoundException:
            print('could not play. make sure sounds path (inside config file) is correct.', file=stderr)
    return ret


def soundify(command):
    '''
    soundify a command.
    run command as another process, check exit code and play related sound
    '''
    # run the command in new process
    try:
        proc = Popen(command.split())
        proc.wait()
    except FileNotFoundError:
        print('command not found.', file=stderr)
        return 127 

    # capture return code, play sound
    ret = proc.returncode

    Popen(['soundify', '--test', str(ret)], stderr=DEVNULL, stdout=DEVNULL)

    # keep return code
    return ret

