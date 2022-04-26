#!/usr/bin/python3
from time import sleep

import autostart
import wifi
from utils.shell_util import shell


def encrypt_file(file, out_file, passw):
    shell(f"openssl enc -aes-256-cbc -in {file} -out {out_file} -iter 10000000 -pass pass:{passw}")
    pass


def decript_file(file, out_file, passw):
    shell(f"openssl aes-256-cbc -in {file} -out {out_file} -iter 10000000 -pass pass:{passw}")
    pass


if __name__ == '__main__':
    pass
