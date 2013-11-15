#!/usr/bin/env python

import sys

city_clusters = {}
user_records = []

def get_data():
	global city_clusters
	global user_records

	for line in sys.stdin:
		line = line.strip()
		record = []
		record = line.split('\t')
		if len(record) == 3:
			city_clusters[record[1]] = record[2]
		else:
			user_records.append(record)

def cluster_users():
	for record in range(0, len(user_records)):
		print '%s\t%s\t%s\t%s\t%s\t%s' % (user_records[record][0], user_records[record][1], 
			user_records[record][2], user_records[record][3], user_records[record][4], city_clusters[user_records[record][3]])

def reducer():
	get_data()
	cluster_users()

if __name__=='__main__':
	reducer()