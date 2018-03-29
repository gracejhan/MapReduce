#!/usr/bin/env python

# Big Data Assignment 1 - Task7
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_violation_code = None
violation_code = None
weekday_cnt = 0
weekend_cnt = 0
date = None
weekend = [5,6,12,13,19,20,26,27]
ignore = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if not line:
        continue
    if '\t' not in line:
        continue

    # key = violation_code
    # value = weekday_avg, weekend_avg

    # parse the input we got from mapper.py
    violation_code, date = line.split('\t', 1)

    # if the data is not a date ignore it
    if len(date) != 10:
        ignore += 1
        continue

    # date is in format YYYY-MM-DD
    day = date[8:10]
    day = int(day)

    # If we were previously working on this violation_code...
    if current_violation_code == violation_code:
        if day in weekend:
            weekend_cnt += 1
        else:
            weekday_cnt += 1

    # If this is a new violation_code...
    else:
        # But not a first one...
        if current_violation_code:
            weekday_avg = weekday_cnt / float(23)
            weekend_avg = weekend_cnt / float(8)
            print('%s\t%.2f, %.2f' % (current_violation_code, weekend_avg,
                                      weekday_avg))
        # reset data to current ones
        if day in weekend:
            weekend_cnt = 1
            weekday_cnt = 0
        else:
            weekend_cnt = 0
            weekday_cnt = 1
        current_violation_code = violation_code

# output for the last violation_code
if current_violation_code == violation_code:
    weekday_avg = weekday_cnt / float(23)
    weekend_avg = weekend_cnt / float(8)
    print('%s\t%.2f, %.2f' % (current_violation_code, weekend_avg,
                              weekday_avg))

# print('Number IGNORED: %d' % ignore)
