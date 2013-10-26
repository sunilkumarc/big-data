#!/usr/bin/env python
import sys

def emit():
	for line in sys.stdin:
	    line = line.strip()
	    print line

def mapper():
	emit()

if __name__=='__main__':
	mapper()