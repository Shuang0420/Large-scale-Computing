#!/usr/bin/python
import sys


for line in sys.stdin:
    #split the line into words
    res = line.strip().split('\t', 1)
    print '%s\t%s' % (res[1], res[0])
