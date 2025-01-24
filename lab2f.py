#!/usr/bin/env

# Author: Bakari Taylor
# Author ID: 183099233
# Date Created: 2025/01/22

import sys


arguments = sys.argv
script = sys.argv[0]
timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')