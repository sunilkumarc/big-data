#!/usr/bin/env python

import sys
import json
from pprint import pprint
import random

adds = {
	"outliers":["Advertisement1(outliers)", "Advertisement2(outliers)", "Advertisement3(outliers)", "Advertisement4(outliers)", "Advertisement5(outliers)"],
	"0-15":["Advertisement1(0-15)", "Advertisement2(0-15)", "Advertisement3(0-15)", "Advertisement4(0-15)", "Advertisement5(0-15)"],
	"16-30":["Advertisement1(16-30)", "Advertisement2(16-30)", "Advertisement3(16-30)", "Advertisement4(16-30)", "Advertisement5(16-30)"],
	"31-50":["Advertisement1(31-50)", "Advertisement2(31-50)", "Advertisement3(31-50)", "Advertisement4(31-50)", "Advertisement5(31-50)"],
	"gt-50":["Advertisement1(gt-50)", "Advertisement2(gt-50)", "Advertisement3(gt-50)", "Advertisement4(gt-50)", "Advertisement5(gt-50)"]
}

user_records = []
user_ids = []
cluster_ids = []
distance_matrix = []
main_clusters = []
age_0_15 = []
age_16_30 = []
age_31_50 = []
age_gt_50 = []

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

	print 'Total no of users : ', len(user_records)

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

	main_clusters.append(each_cluster)

	
def make_age_clusters():
	print 'Outliers : '
	print 'No of users : ', len(main_clusters[0])
	add_outliers = adds['outliers']
	print 'Age group (0-15) : ', add_outliers[random.randint(0, len(add_outliers)-1)]
	print 'Age group (16-30) : ', add_outliers[random.randint(0, len(add_outliers)-1)]
	print 'Age group (31-50) : ', add_outliers[random.randint(0, len(add_outliers)-1)]
	print 'Age group (gt-50) : ', add_outliers[random.randint(0, len(add_outliers)-1)]
	print

	for i in range(1, len(main_clusters)):
		global age_0_15
		global age_16_30
		global age_31_50
		global age_gt_50
		for row in main_clusters[i]:
			if int(row[4]) <= 15:
				age_0_15.append(row)
			elif int(row[4]) <= 30:
				age_16_30.append(row)
			elif int(row[4]) <= 50:
				age_31_50.append(row)
			else:
				age_gt_50.append(row)

		print 'Cluster - ', i
		print 'No of users : ', len(main_clusters[i])
		add_0_15 = adds['0-15']
		print 'Age group (0-15) : ', add_0_15[random.randint(0, len(add_0_15)-1)]

		add_16_30 = adds['16-30']
		print 'Age group (16-30) : ', add_16_30[random.randint(0, len(add_16_30)-1)]

		add_31_50 = adds['31-50']
		print 'Age group (31-50) : ', add_31_50[random.randint(0, len(add_31_50)-1)]
		
		add_gt_50 = adds['gt-50']
		print 'Age group (gt-50) : ', add_gt_50[random.randint(0, len(add_gt_50)-1)]
		print

def reducer():
	get_data()
	process_records()
	make_age_clusters()

if __name__=='__main__':
	reducer()