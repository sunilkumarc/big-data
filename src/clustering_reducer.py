import sys

for line in sys.stdin:
	line = line.strip()
	city, location = line.split('\t', 1)
	
	print '%s\t%s' % (city, location)