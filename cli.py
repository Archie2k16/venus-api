#!/usr/bin/env python
# encoding:utf-8
# me@archie.cc

help_prompt='''
The venus help:
'''
import sys
from tools.mapping import m21
from wsgi import run

d = m21({('-m', 'manage'): 1,
         ('-v', 'version'): 3,
         ('-h', 'help'): 2,
         ('-c', 'config'): 5}
        )

def show_help():
    print help_prompt

def start():
    if len(sys.argv) == 1:
        run()
    elif len(sys.argv) == 2:
        show_help()
