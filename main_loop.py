#!/usr/bin/python3
import sys, os
from time import sleep

import autostart
from utils.shell_util import shell


def pull_git():
    commit = shell("git rev-parse HEAD")
    shell("git pull -f -q")
    commit2 = shell("git rev-parse HEAD")
    return commit != commit2


if __name__ == '__main__':
    me_file = os.path.abspath(sys.argv[0])
    pwd = os.path.dirname(os.path.realpath(__file__))
    print("pwd: " + pwd)

    commit = shell("git rev-parse HEAD")
    print(f"acrobat started on commit {commit}")

    shell("sudo " + os.path.join(pwd, "iptables.sh"))

    autostart.setup_autostart()

    while True:
        if pull_git():
            print(f"acrobat restart after update from remote")
            os.execl("/usr/bin/python3", "/usr/bin/python3", sys.argv[0])
            exit(0)

        sleep(60 * 60 * 24)
