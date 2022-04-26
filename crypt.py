#!/usr/bin/python3
import os
from time import sleep

import autostart
import wifi
from utils.shell_util import shell
import argparse


def encrypt_file(file, out_file, passw):
    shell(f"openssl enc -aes-256-cbc -in {file} -out {out_file} -iter 100 -pass pass:{passw}")
    pass


def decript_file(file, out_file, passw):
    shell(f"openssl enc -aes-256-cbc -d -in {file} -out {out_file} -iter 100 -pass pass:{passw}")
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cryp configs')
    parser.add_argument('-d', action='store_true', help="decrypt")
    parser.add_argument('-e', action='store_true', help="encrypt")
    parser.add_argument('--in_file', help='source file', required=True)
    parser.add_argument('--out_file', help='outfile file', required=True)
    parser.add_argument('--passw', help='passw, default take from ~/.local/data/my_config_key')
    args = parser.parse_args()

    if args.passw is None:
        with open(os.path.expanduser('~') + "/.local/data/my_config_key", "r") as f:
            args.passw = f.readline()

    if args.d:
        decript_file(args.in_file, args.out_file, args.passw)
        exit(0)
    elif args.e:
        encrypt_file(args.in_file, args.out_file, args.passw)
        exit(0)
    else:
        print("add -d or -e")
        parser.print_help()
        exit(0)

    pass
