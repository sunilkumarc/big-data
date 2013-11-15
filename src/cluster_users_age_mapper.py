#!/usr/bin/env python
import sys

user_records = []
user_ids = []
cluster_ids = []

def get_data():
	global user_records

	for line in sys.stdin:
		line = line.strip()
		record = []
		line = line.split('\t')
		record = line[:(len(line)-1)]
		cluster_id = line[(len(line)-1):][0]
		user_records.append(record)
		cluster_ids.append(cluster_id)

def emit():
	for i in range(0, len(user_records)):
		print '%d' % int(cluster_ids[i]),
		for j in range(0, len(user_records[i])):
			print '\t%s' % (user_records[i][j]),
		print

def mapper():
	get_data()
	emit()

if __name__=='__main__':
	mapper()
