'''
functions related to main

@authors:
    - @amiremohamadi

changelogs:
    - nothing
'''

from config import read_config
from subprocess import Popen
from playsound import playsound


def soundify(command):
    '''
    soundify a command.
    run command as another process, check exit code and play related sound
    '''

    # a map from error_code to sound_dir
    err_sound = read_config()

    # run the command in new process
    proc = Popen(command)
    proc.wait()

    # capture return code, play sound
    ret = proc.returncode

    sound = err_sound.get(ret, None)
    if sound:
        # TODO: Popen playsound
        pass

    # keep return code
    return ret

