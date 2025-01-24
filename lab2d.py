#!/usr/bin/env python3

import sys


arguments = sys.argv
script = sys.argv[0]
name = sys.argv[1]
age = sys.argv[2]

if len(sys.argv) != 3:
    print('you do not have 2 arguments')
    sys.exit()

print('Hi ' + sys.argv[1] + ', you are ' + sys.argv[2] + ' years old.')
