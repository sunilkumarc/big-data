#!/usr/bin/python2.7
import math, sys
from utils import *
import Queue
import itertools

# take the 1st command line argument as the filename
if len(sys.argv) < 4:
	print "arguments - filename epsilon mu"
	sys.exit(0)
filename = sys.argv[1]
ep = float(sys.argv[2])
mu = int(sys.argv[3])

# build the matrix from the file
matrix = readFileAsMatrix(filename)
# get the size of the matrix (n x n)
n = len(matrix)

# build the lambda set for each vertex i
lambdaSets = getLambdaSets(matrix)

# build a matrix of sigma(u, v) for all pairs (u, v)
sigmaMatrix = getSigmaMatrix(matrix, lambdaSets)

# build the neighbourhood set for each vertex i
nhoodSets = getNhoodSets(matrix, lambdaSets, sigmaMatrix, ep)

# implementation of the algo
vertex_label = ["" for i in range(0, n)]
cluster_label = [None for i in range(0, n)]

i = 0
for u in range(0, n):
	if isCore(nhoodSets[u], mu):
		cluster_id = "cluster-" + str(i)
		q = Queue.Queue()
		for v in nhoodSets[u]:
			q.put(v)
		while q.empty() == False:
			w = q.get()
			R = [j for j in range(0, n) if matrix[w][j] > 0]
			for s in R:
				if vertex_label[s] == "" or vertex_label[s] != Label.NONMEMBER:
					vertex_label[s] = cluster_id
					cluster_label[s] = i
		i += 1
	else:
		vertex_label[u] = Label.NONMEMBER

for u in [i for i in range(0, n) if vertex_label[i] == Label.NONMEMBER]:
	pairFound = False
	for pair in itertools.combinations([i for i in range(0, n) if sigmaMatrix[u][i] > 0], 2):
		if cluster_label[pair[0]] != None and cluster_label[pair[1]] != None and cluster_label[pair[0]] != cluster_label[pair[1]]:
			vertex_label[u] = Label.HUB
			pairFound = True
			break
	if not pairFound:
		vertex_label[u] = Label.OUTLIER

print "  Vertex  |  Label  "
print "==========|=========="
for i in range(0, n):
	print ("   %4d  " % i) + " | " + vertex_label[i]
