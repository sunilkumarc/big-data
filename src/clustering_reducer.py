#!/usr/bin/env python

import sys

location_ids = []
coordinates = []
def fun():
	for line in sys.stdin:
		line = line.strip()
		city, location_id, latitude, longitude = line.split('\t')
		location_ids.append(location_id)

		coordinate = []
		coordinate.append(latitude)
		coordinate.append(longitude)
		coordinates.append(coordinate)
		#print '%s' % (city)

	#print location_ids
	print coordinates

if __name__=='__main__':
	fun()