#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split("\t")
    
    # for column in columns:
    #     print '%s\t%s' % (column, 1)
    print "%s\t%s" % (columns[0], columns[1])

