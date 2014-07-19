#!/usr/bin/env python

# Simple script to open up Mac's version of windowed emacs from command line

import os
import os.path
import subprocess
import sys

args = sys.argv[1:]

for i in range(len(args)):
    args[i] = os.path.abspath(args[i])

subprocess.call(["open", "/Applications/Emacs.app/", "--args"] + args)
