#!/usr/bin/env python

# Big Data Assignment 1 - Task7
# Jungwoo Han (jh5990@nyu.edu)

import csv
import sys
import string

# input comes from STDIN (standard input)
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    violation_code = entry[2]
    issue_date = entry[1]

    print('%s\t%s' % (violation_code, issue_date))
