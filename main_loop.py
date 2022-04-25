#!/usr/bin/python3
from time import sleep

from utils.shell_util import shell

if __name__ == '__main__':

    while True:
        shell("git pull")

        sleep(60 * 60 * 24)
