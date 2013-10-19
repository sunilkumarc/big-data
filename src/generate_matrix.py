#!/bin/python2

import sys

lines = []
with open(sys.argv[1]) as f:
    lines = f.readlines()

def parse_meta(lines):
    n = len(lines)
    for i in range(0, n):
        line = lines[i].strip()
        if line.find("%%") < 0:
            pass # TODO
        else:
            return lines[i+1:]
        ++i
    return null

def parse_data(lines):
    id = 0
    v = {}
    e = []
    for line in lines:
        line = line.strip()
        if line.find(":") < 0:
            v[line] = id
            id += 1
        else:
            e.append(line)

    matrix = [[0 for i in range(len(v.keys()))] for i in range(len(v.keys()))]
    for edge in e:
        vertices, weight = edge.split(":")
        x, y = vertices.split(",")
        matrix[v[x]][v[y]] = weight
        matrix[v[y]][v[x]] = weight

    # Judgement call. mat[i][i] is taken to be zero
    #for i in range(len(v.keys())):
    #    matrix[i][i] = -1
        
    for row in matrix:
        for col in row:
            print col,
        print

def parse_lines(lines):
    parse_data(parse_meta(lines))

parse_lines(lines)