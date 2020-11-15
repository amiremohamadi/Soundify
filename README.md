
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
