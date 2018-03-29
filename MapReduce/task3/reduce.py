#!/usr/bin/env python

# Big Data Assignment 1 - Task3
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_license_type = None
total_amount = 0
license_type = None
count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if not line:
        continue
    if '\t' not in line:
        continue

    # key = license_type
    # value = amount_due_total, amount_due_average

    # parse the input we got from mapper.py
    license_type, amount = line.split('\t', 1)

    # convert amount (currently a string) to float
    try:
        amount = float(amount)
    except ValueError:
        # amount was not a number, so silently
        # ignore/discard this line
        continue

    # If we were previously working on this license_type...
    if current_license_type == license_type:
        total_amount = total_amount + amount
        count = count + 1
    # If this is a new license_type...
    else:
        # But not a first one...
        if current_license_type:
            average = total_amount / float(count)
            # print the previous license_type's key-value pair
            print('%s\t%.2f, %.2f' % (current_license_type, total_amount, average))
        # reset data to current ones
        total_amount = amount
        current_license_type = license_type
        count = 1

# output for the last license_type
if current_license_type == license_type:
    average = total_amount / float(count)
    print('%s\t%.2f, %.2f' % (current_license_type, total_amount, average))
