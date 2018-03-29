#!/usr/bin/env python

# Big Data Assignment 1 - Task6
# Jungwoo Han (jh5990@nyu.edu)

import sys
import string
import csv

# input comes from STDIN (standard input)
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    plate_id = entry[14]
    registration_state = entry[16]

    print('%s, %s\t1' % (plate_id, registration_state))
