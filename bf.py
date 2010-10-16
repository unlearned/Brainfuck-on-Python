#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from brainfuck import Brainfuck


if __name__ == '__main__':

    argvs = sys.argv
    argc = len(argvs)

    if (argc != 2):
        print 'Usage: $ %s filename' % argvs[0]
        quit()


    f = open(argvs[1], 'r')
    lines = f.readlines()

    context = Brainfuck()
    for line in lines:
        if re.match(r'^#!', line):
            continue

        context.readScript(line)

    context.exe()

    print ""
    quit()

