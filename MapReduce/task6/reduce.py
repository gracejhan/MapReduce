#!/usr/bin/env python

# Big Data Assignment 1 - Task6
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys
# the system python does not have numpy, but the python/gnu/2.7.10 does
# (we don't actually need it, but attempting to import it will trigger
# an error if the mapper can't see the version of python we want to use)
#import numpy

current_key = None
key = None
data_max = []

for line in sys.stdin:

    try:
        line = line.strip()
        key, count = line.split('\t')
    except ValueError:
        continue

    if current_key == key:
        current_count += 1

    else:
        if current_key:

            data_max.append((current_key, current_count))
        data_max.sort(key = lambda x:x[1], reverse = True)
        data_max = data_max[:20]

        current_key = key
        current_count = 1

for pair in data_max:
    print('%s\t%d'%(pair[0],pair[1]))
