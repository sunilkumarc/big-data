#!/usr/bin/env python

import sys
from math import radians, sin, cos, asin, sqrt
import numpy as np
from sklearn.cluster import DBSCAN

location_ids = []
coordinates = []
distance_matrix = []

def get_data():
	coordinates =  [[  9.31814191 ,  3.05936398],[ 11.33116579 ,  3.49705635],[  7.40307657 , -8.3921121 ],[ -5.7490319  ,  9.35116312],[  8.70727802 , -6.86474419],[  8.90656607 , -7.08469764],[ 10.87461195  , 1.83111066],[ -4.99664395 ,  9.21298913],[ -3.86794767 ,  9.58207358],[  7.47731822 , -7.10745072],[ -4.98751978 , 10.70935837],[ 10.30312819   ,3.45629108],[  9.32730694  ,-6.06141136],[ 10.71365374   ,3.05349328],[ -3.2448011 ,9.94528279]]

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
	distance_matrix = np.array(distance_matrix)
	similarity_matrix = 1 - (distance_matrix/(np.max(distance_matrix))
	db = DBSCAN().fit_predict(similarity_matrix)
	print db


def reducer():
	get_data()
	calculate_distance_matrix()
	cluster()

if __name__=='__main__':
	reducer()