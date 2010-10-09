#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from brainfuck import Brainfuck


if __name__ == '__main__':

    argvs = sys.argv
    argc = len(argvs)

    if (argc != 2):
        print 'Usage: $ %s filename' % argvs[0]
        quit()


    f = open(argvs[1], 'r')
    lines = f.readlines()

    script = ''
    for line in lines:
        script += line
        
    fuck = Brainfuck()
    fuck.readScript(script)
    fuck.exe()

    print ""
    quit()

