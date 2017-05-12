#!/usr/bin/env python

from operator import itemgetter
import sys
from itertools import groupby


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple node-count pairs by node,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_node - string containing a node (the key)
    #   group - iterator yielding all ["&lt;current_node&gt;", "&lt;count&gt;"] items
    for current_node, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_node, count in group)
            print "%s%s%d" % (current_node, separator, total_count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()
