#!/usr/bin/env python

# Big Data Assignment 1 - Task4
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_registration_state = None
registration_state = None
total_count = 0
other_sum = 0
ny_sum = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if not line:
        continue
    if '\t' not in line:
        continue

    # key = registration_state ('NY' or 'Other')
    # value = count

    # parse the input we got from mapper.py
    registration_state, count = line.split('\t', 1)

    # convert amount (currently a string) to float
    try:
        count = int(count)
    except ValueError:
        # amount was not a number, so silently
        # ignore/discard this line
        continue

    # If we were previously working on this registration_state...
    if current_registration_state == registration_state:
        total_count = total_count + 1
    # If this is a new registration_state...
    else:
        # But not a first one...
        if current_registration_state:
            if current_registration_state == 'NY':
                ny_sum = ny_sum + total_count
            if current_registration_state == 'Other':
                other_sum = other_sum + total_count
        # reset data to current ones
        total_count = 1
        current_registration_state = registration_state

# output for the last registration_state
if current_registration_state == registration_state:
    if current_registration_state == 'NY':
        ny_sum = ny_sum + total_count
    if current_registration_state == 'Other':
        other_sum = other_sum + total_count
if other_sum != 0:
    print('%s\t%d' % ('Other', other_sum))
if ny_sum != 0:
    print('%s\t%d' % ('NY', ny_sum))
