#!/usr/bin/env python

# task2

import sys
import string

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    entry = line.split(",")

    # key = violation_code
    # value = 1
    violation_code = entry[2]

    print('%s\t1' % violation_code)
