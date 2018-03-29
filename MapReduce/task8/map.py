#!/usr/bin/env python

# Big Data Assignment 1 - Task8
# Jungwoo Han (jh5990@nyu.edu)
import csv
import sys
import string

# input comes from STDIN (standard input)
for line in csv.reader(sys.stdin,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
    entry = line

    vehicle_make = entry[20]
    vehicle_color = entry[19]

    if not vehicle_make:
        vehicle_make = 'NONE'
    if not vehicle_color:
        vehicle_color = 'NONE'

    if vehicle_make:
        print('vehicle_make^ %s\t1' % (vehicle_make))
    if vehicle_color:
        print('zvehicle_color^ %s\t1' % (vehicle_color))
