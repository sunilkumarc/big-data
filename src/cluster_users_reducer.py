#!/usr/bin/env python
import sys

cities_cluster = {}

def get_data():
	# Need to change this also.
	global cities_cluster

	for line in sys.stdin:
	    line = line.strip()
	    # city_id, city, cluster = line.split('\t')
	    # if city_id == '-1' and city == '-1' and cluster == '-1':
	    # 	break
	    # else:
	    # 	cities_cluster[city] = cluster
	    print line

	# for line in sys.stdin:
	# 	line = line.strip()
	# 	user_id, first, last, city = line.split('\t')
	# 	print '%s\t%s\t%s\t%s' % (user_id, first, last, city)

def reducer():
	get_data()
	# print cities_cluster

if __name__=='__main__':
	reducer()