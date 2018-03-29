#!/usr/bin/env python

# Big Data Assignment1 - Task1
# Name: Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_summons = None
summons = None
summons_dict = {}
current_list = []
final_list = []

for line in sys.stdin:
    line = line.strip()

    summons, values = line.split('\t',1)

    value_list = values

    # if summons is not new do...
    if current_summons == summons:
        # add values to the old values list
        current_list = current_list + value_list

    else:
        # if summons is new but not the first one do...
        if current_summons:
            if 'unpaid' not in current_list:
                print("%s\t%s" % (current_summons, current_list))

        # do this for all new summons
        current_summons = summons
        current_list = value_list

if 'unpaid' not in current_list:
    print("%s\t%s" % (current_summons, current_list))

