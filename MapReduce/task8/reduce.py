#!/usr/bin/env python

# Big Data Assignment 1 - Task8
# Jungwoo Han (jh5990@nyu.edu)

from operator import itemgetter
import sys

current_feature = None
current_spec = None
spec_cnt = 0
feature = None
spec = None


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    pair, count = line.split('\t', 1)

    # feature is Make or Color
    # spec is the types of Makes or Colors
    feature, spec = pair.split("^")
    if feature == 'zvehicle_color':
        feature = 'vehicle_color'

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: code) before it is passed to the reducer
    if ((current_feature == feature) and (current_spec == spec)):
        spec_cnt += 1
    else:
        if current_feature:
            # write result to STDOUT
            print('%s\t%s, %d' % (current_feature, current_spec, spec_cnt))
        current_feature = feature
        current_spec = spec
        spec_cnt = 1

# do not forget to output the last code if needed!
if ((current_feature == feature) and (current_spec == spec)):
    print('%s\t%s, %d' % (current_feature, current_spec, spec_cnt))
