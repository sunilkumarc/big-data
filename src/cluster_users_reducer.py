#!/usr/bin/env python
import sys

def reducer():
	for line in sys.stdin:
		line = line.strip()
		print line

if __name__=='__main__':
	reducer()