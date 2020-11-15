from codecs     import open
from inspect    import getsource
from os.path    import abspath, dirname, join
from setuptools import setup

setup(name             = 'soundify',
      packages         = ['soundify'],
      version          = '0.4',

      install_requires = [
        'playsound',
        'pyyaml'
      ],

      description      = 'soundify exitcodes',
      url              = 'https://github.com/amiremohamadi/Soundify',
      author           = 'amiremohamadi',
      license          = 'GPL V2.0',
      classifiers      = [
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.3',
                          'Programming Language :: Python :: 2.4',
                          'Programming Language :: Python :: 2.5',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.1',
                          'Programming Language :: Python :: 3.2',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Programming Language :: Python :: 3.5',
                          'Topic :: Multimedia :: Sound/Audio :: MIDI',
                          'Topic :: Multimedia :: Sound/Audio :: Players',
                          'Topic :: Multimedia :: Sound/Audio :: Players :: MP3'],
      keywords         = 'sound playsound music wave wav mp3 media song play audio',
      py_modules       = ['soundify'],

      entry_points = {
          "console_scripts": ["soundify = soundify.__main__:main"]
      }
)
