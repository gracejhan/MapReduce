#!/usr/bin/env python

# Big Data Assignment 1 - Task5
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_registration_state = None
registration_state = None
current_plate_id = None
plate_id = None
count = 0
max_count = 0
max_reg_state = None
max_plate_id = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if not line:
        continue
    if '\t' not in line:
        continue

    # key = registration_state, plate_id
    # value = count

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    registration_state, plate_id = key.split(",")

    registration_state = registration_state.upper()
    plate_id = plate_id.upper()

    # If we were previously working on this person...
    if ((current_registration_state == registration_state) and \
        (current_plate_id == plate_id)):
        count = count + 1
    # If this is a new registration_state...
    else:
        # But not a first one...
        if current_registration_state:
            # update the maximum violation data if applicable
            if count > max_count:
                max_count = count
                max_reg_state = current_registration_state
                max_plate_id = current_plate_id
        # reset data to current ones
        count = 1
        current_registration_state = registration_state
        current_plate_id = plate_id

# output for the last registration_state
if ((current_registration_state == registration_state) and \
    (current_plate_id == plate_id)):
    if count > max_count:
        max_count = count
        max_reg_state = current_registration_state
        max_plate_id = current_plate_id

# print the key-value pair with maximum violation count
print('%s, %s\t%d'%(max_reg_state, max_plate_id, max_count))
