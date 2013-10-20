#!/usr/bin/env python

import sys
from math import radians, sin, cos, asin, sqrt

location_ids = []
coordinates = []
distance_matrix = []

def get_data():
	for line in sys.stdin:
		line = line.strip()
		location_id, city, latitude, longitude = line.split('\t')
		location_ids.append(location_id)

		coordinate = []
		coordinate.append(latitude)
		coordinate.append(longitude)
		coordinates.append(coordinate)
		#print '%s' % (city)

	#print location_ids
	print coordinates
	print location_ids

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
	distance_matrix = [[None]*len(location_ids)]*len(location_ids)

	for coordinate1 in range(0, len(coordinates)):
		lat1 = coordinates[coordinate1][0]
		long1 = coordinates[coordinate1][1]

		for coordinate2 in range(0, len(coordinates)):
			lat2 = coordinates[coordinate2][0]
			long2 = coordinates[coordinate2][1]
			# print '(',lat1,',',long1,') ----', '(',lat2,',',long2,')'
			
			lat1 = float(lat1)
			long1 = float(long1)
			lat2 = float(lat2)
			long2 = float(long2)
			if(coordinate1 == coordinate2):
				# print coordinate1, coordinate2
				distance_matrix[coordinate1][coordinate1] = 0
			else:
				# print coordinate1, coordinate2
				# distance_matrix[coordinate1][coordinate2] = calculate_distance(lat1, long1, lat2, long2)
				distance_matrix[coordinate1][coordinate2] = 1

	# print distance_matrix[0][4]
	print distance_matrix

def reducer():
	get_data()
	calculate_distance_matrix()

	# for i in range(0, len(location_ids)):
	# 	for j in range(0, len(location_ids)):
	# 		print distance_matrix[i][j],
	# 	print

if __name__=='__main__':
	reducer()