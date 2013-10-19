import math

# function to create enum
def enum(**enums):
    return type('Enum', (), enums)
Label = enum(NONMEMBER='nonmember', HUB='hub', OUTLIER='outlier')

# function to create a matrix from a file with name "filename"
def readFileAsMatrix(filename):
	f = open(filename)
	lines = f.readlines()
	matrix = [[int(i) for i in line.split()] for line in lines]
	f.close()
	return matrix

# function to print a matrix
def printMatrix(matrix):
	for row in matrix:
		for cell in row:
			print "%.3f" % cell,
		print

# function to compute the lambda set of a vertex x
def getLambdaSet(matrix, x):
	n = len(matrix)
	return [i for i in range(0, n) if matrix[x][i] == 1] + [x]

# function to compute the lambda set for all vertices 
def getLambdaSets(matrix):
	n = len(matrix)
	return [getLambdaSet(matrix, i) for i in range(0, n)]

# function to compute a matrix with sigma(u, v) for a cell in row=u and col=v
def getSigmaMatrix(matrix, lambdaSets):
	n = len(matrix)
	return [[len(set(lambdaSets[u]).intersection(set(lambdaSets[v]))) / math.sqrt(len(lambdaSets[u]) * len(lambdaSets[v])) for v in range(0, n)] for u in range(0, n)]

# function to compute the neighbourhood for a vertex x
def getNhoodSets(matrix, lambdaSets, sigmaMatrix, e):
	n = len(matrix)
	return [[v for v in lambdaSets[u] if sigmaMatrix[u][v] > e] for u in range(0, n)]

def isCore(nhoodSet, mu):
	return len(nhoodSet) >= mu