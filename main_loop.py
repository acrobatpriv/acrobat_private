#!/usr/bin/python3
import sys
from time import sleep

import autostart
import wifi
from utils.shell_util import shell


def pull_git():
    commit = shell("git rev-parse HEAD")
    shell("git pull -f -q")
    commit2 = shell("git rev-parse HEAD")
    return commit != commit2


if __name__ == '__main__':

    me_file = sys.argv[0]

    commit = shell("git rev-parse HEAD")
    print(f"acrobat started on commit {commit}")
    while True:
        if pull_git():
            print(f"acrobat restart after update from remote")
            exec(f"python3 {me_file}")
            exit(0)

        autostart.setup_autostart()
        wifi.setup_wifi()

        sleep(10)
