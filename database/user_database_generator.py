#! /usr/bin/python

import random
import sys

first_name = []
last_name = []
cities = []

def get_data():
	global first_name
	global last_name
	global cities

	names_file = open('names', 'r')
	cities_database = open('cities_database', 'r')

	for line in names_file:
		line = line.strip()
		first, last = line.split('\t')
		first_name.append(first)
		last_name.append(last)

	for city in cities_database:
		city = city.strip()
		city = city.split('\t')
		cities.append(city[1])

def generate_users():
	try:
		no_of_users = int(sys.argv[1])
		user_database = open('user_database', 'w')
		
		for user_id in range(1, no_of_users+1):
			i = random.randint(0, len(first_name)-1)
			j = random.randint(0, len(last_name)-1)
			k = random.randint(0, len(cities)-1)
			age = random.randint(10, 60)
			line = str(user_id) + '\t' + first_name[i] + '\t' + last_name[j] + '\t' + cities[k] + '\t' + str(age) + '\n'
			user_database.write(line)
	except IndexError:
		print 'Enter no of users to generate database'

if __name__=='__main__':
	get_data()
	generate_users()
