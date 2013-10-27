#!/usr/bin/env python

import sys
from math import radians, sin, cos, asin, sqrt
import numpy as np
from sklearn.cluster import DBSCAN

location_ids = []
coordinates = []
distance_matrix = []
similarity_matrix = []
db = []
cities = []

def get_data():
	global location_ids
	global city
	for line in sys.stdin:
		line = line.strip()
		location_id, city, latitude, longitude = line.split('\t')
		location_ids.append(location_id)

		coordinate = []
		coordinate.append(latitude)
		coordinate.append(longitude)
		coordinates.append(coordinate)
		cities.append(city)


def calculate_distance(lat1, long1, lat2, long2):
	lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
	dlat = lat2 - lat1
	dlon = long2 - long1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	km = 6367 * c
	return km


def calculate_distance_matrix():
	global distance_matrix
	distance_matrix = [[None for i in range(0, len(location_ids))] for j in range(0, len(location_ids))]

	for x in range(0, len(coordinates)):
		lat1 = coordinates[x][0]
		long1 = coordinates[x][1]

		for y in range(0, len(coordinates)):
			lat2 = coordinates[y][0]
			long2 = coordinates[y][1]
			
			lat1 = float(lat1)
			long1 = float(long1)
			lat2 = float(lat2)
			long2 = float(long2)
			distance_matrix[x][y] = calculate_distance(lat1, long1, lat2, long2)
		distance_matrix[x][x] = 0

def cluster():
	global distance_matrix
	global similarity_matrix
	global db
	distance_matrix = np.array(distance_matrix)
	similarity_matrix = 1 - (distance_matrix/(np.max(distance_matrix)))
	db = DBSCAN(eps=0.2, min_samples=2).fit_predict(similarity_matrix)

def emit():
	for i in range(0, len(location_ids)):
		print '%d\t%s\t%d' % (int(location_ids[i]), cities[i], db[i])

def reducer():
	get_data()
	calculate_distance_matrix()
	cluster()
	emit()
	
if __name__=='__main__':
	reducer()