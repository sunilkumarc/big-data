#!/usr/bin/env python
import sys

def emit():
	# Need to change here. This is not going to work
	for line in sys.stdin:
	    line = line.strip()
	    city_id, city, cluster = line.split('\t')
	    if city_id == '-1' and city == '-1' and cluster == '-1':
	    	break
	    else:
	    	print '%s\t%s\t%s' % (city_id, city, cluster)

	for line in sys.stdin:
		line = line.strip()
		user_id, first, last, city = line.split('\t')
		print '%s\t%s\t%s\t%s' % (user_id, first, last, city)

def mapper():
	emit()

if __name__=='__main__':
	mapper()