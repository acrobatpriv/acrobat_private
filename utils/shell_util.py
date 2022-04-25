import os, sys
import subprocess


def shell(cmd):
    out = subprocess.run(cmd.split(' '), capture_output=True, text=True)
    return out.stdout
