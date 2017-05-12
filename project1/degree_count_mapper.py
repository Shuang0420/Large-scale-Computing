#!/usr/bin/python
import re
import sys
import os


for line in sys.stdin:
    #split the line into words
    nodes = line.strip().split('\t')
    print '%s\t%s' % (nodes[0], 1)
    print '%s\t%s' % (nodes[1], 1)
