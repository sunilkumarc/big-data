#!/usr/bin/env python
import sys

user_records = []
user_ids = []
cluster_ids = []
distance_matrix = []
main_clusters = []

def get_data():
	global user_records
	global user_ids
	global cluster_ids

	for line in sys.stdin:
		line = line.strip()
		line = line.split('\t')
		cluster_id = line[0]
		user_record = line[1:]
		print user_record
		cluster_ids.append(cluster_id)
		user_records.append(user_record)
		

def process_records():
	previous_id = cluster_ids[0]
	global main_clusters
	each_cluster = []
	for i in range(0, len(user_records)):
		current_id = cluster_ids[i]
		if(current_id == previous_id):
			each_cluster.append(user_records[i])
		else:
			main_clusters.append(each_cluster)
			each_cluster = []
			each_cluster.append(user_records[i])
			previous_id = current_id

def reducer():
	get_data()
	process_records()

if __name__=='__main__':
	reducer()

