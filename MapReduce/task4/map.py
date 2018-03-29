#!/usr/bin/env python

# Big Data Assignment 1 - Task4
# Jungwoo Han (jh5990@nyu.edu)
import csv
import sys
import string

# input comes from STDIN (standard input)
# for line in sys.stdin:
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    registration_state = entry[16]

    if registration_state != 'NY':
        registration_state = 'Other'

    print('%s\t1' % (registration_state))
