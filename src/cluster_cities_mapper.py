#!/usr/bin/env python

import sys

def emit():
	for line in sys.stdin:
	    line = line.strip()
	    columns = line.split("\t")
	    
	    print "%s\t%s\t%s\t%s" % (columns[0], columns[1], columns[2], columns[3])

def mapper():
	emit()

if __name__=='__main__':
	mapper()