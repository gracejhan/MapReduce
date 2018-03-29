#!/usr/bin/env python

# task2

from operator import itemgetter
import sys

current_code = None
current_count = 0
code = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    code, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: code) before it is passed to the reducer
    if current_code == code:
        current_count += count
    else:
        if current_code:
            # write result to STDOUT
            print('%s\t%s' % (current_code, current_count))
        current_count = count
        current_code = code

# do not forget to output the last code if needed!
if current_code == code:
    print('%s\t%s' % (current_code, current_count))
