
<p align="center">
<a href="https://www.youtube.com/watch?v=E9kT7NkVCWk" target="_blank">
<img src="https://github.com/amiremohamadi/Soundify/blob/master/youtube_preview.png" width="580">
</a>
</p>

# Soundify
Soundify can play sounds according to exit codes.

## Installation
For stable version:
```sh
$ pip3 install soundify
```

Or manual installation (not necessarily stable):
```sh
$ git clone git@github.com:amiremohamadi/Soundify.git
$ cd Soundify
$ pip3 install .
```

## Configure
You need a config file to tell `soundify`, play which music for what exit code.

1. check config path by:
```sh
$ soundify -c
```

2. create config file 
```sh
$ vim $(soundify -c)
```

it's a yaml file. syntax is like this:
```yaml
0: 'path/to/sound/file'
1: 'path/to/sound/file'
2: 'path/to/sound/file'
error_code: 'path/to/sound/file'
```

**NOTE**: You can test your config:
```sh
$ soundify -t 0
$ soundify -t 1
```
And check if all the configured sounds are playing well or not.

That's it!

**You can find cool sounds from [here](http://soundbible.com/).**

## Usage
```sh
$ soundify your_command
```

**NOTE**: Don't forget to put quotes around your command, if the command
contains spaces.

```sh
$ soundify "gcc main.c -o main"
```

Or you can use it inside a build automation tool (such as Makefile).
assume we have a Makefile like this:

```Makefile
main: main.c
    soundify "gcc main.c -o main"
```

So then just:
```sh
$ make
```

Hooray! :D

**NOTE**: Also soundify doesn't change exit code:
```sh
$ soundify "ls a_file_that_does_not_exist"
$ echo $? # print exit code
```

## Contribute
Soundify is a new small weekend project, it may have lots of
problems. So feel free to contribute.
