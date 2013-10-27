#!/usr/bin/env python

import sys

def emit():
	for line in sys.stdin:
		line = line.strip()
		record = []
		record = line.split('\t')
		if len(record) == 3:
			print '%s\t%s\t%s' % (record[0], record[1], record[2])
		elif len(record) == 5:
			print '%s\t%s\t%s\t%s\t%s' % (record[0], record[1], record[2], record[3], record[4])

def mapper():
	emit()

if __name__=='__main__':
	mapper()