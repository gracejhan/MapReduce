#!/usr/bin/env python

# Big Data Assignment 1 - Task3
# Jungwoo Han (jh5990@nyu.edu)
import csv
import sys
import string

# input comes from STDIN (standard input)
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    license_type = entry[2]
    amount_due = entry[12]

    print('%s\t%s' % (license_type, amount_due))
