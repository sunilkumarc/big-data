#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	city, location = line.split('\t')
	
	print '%s\t%s' % (city, location)