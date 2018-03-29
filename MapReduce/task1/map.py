#!/usr/bin/env python

# Big Data Assignment1 - Task1
# Name: Jungwoo Han (jh5990@nyu.edu)
import csv
import sys
import string
# the system python does not have numpy, but the python/gnu/3.4.4 does
# (we don't actually need it, but attempting to import it will trigger
# an error if the mapper can't see the version of python we want to use)

# remove rows that have NaN values
# parking_violations.dropna(how='any', inplace=True)
# open_violations.dropna(how='any', inplace=True)

# input comes from STDIN (standard input)
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    summons_number = entry[0]

    # If the file is "parking_violations" ...
    if(len(entry) > 18):
        plate_id = entry[14]
        violation_precinct = entry[6]
        violation_code = entry[2]
        issue_date = entry[1]

        print('%s\t%s, %s,  %s, %s' % (summons_number, plate_id,
                                    violation_precinct, violation_code,
                                    issue_date))

    # If the file is "open_violations" ...
    else:
        flag = 'unpaid'
        print('%s\t%s' % (summons_number, flag))
