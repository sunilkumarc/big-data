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
	
def test():
	for i in range(1, len(main_clusters)):
		age_0_15 = []
		age_16_30 = []
		age_31_50 = []
		age_gt_50 = []
		for row in main_clusters[i]:
			if int(row[4]) <= 15:
				age_0_15.append(row)
			elif int(row[4]) <= 30:
				age_16_30.append(row)
			elif int(row[4]) <= 50:
				age_31_50.append(row)
			else:
				age_gt_50.append(row)
	

def reducer():
	get_data()
	process_records()
	test()

if __name__=='__main__':
	reducer()