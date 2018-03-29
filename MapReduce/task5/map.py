#!/usr/bin/env python

# Big Data Assignment 1 - Task5
# Jungwoo Han (jh5990@nyu.edu)

import sys
import string

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    entry = line.split(",")

    # key = license_type
    # value = amount_due
    plate_id = entry[14]
    registration_state = entry[16]

    print('%s, %s\t1' % (plate_id, registration_state))
