#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 13."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import numpy as np

DESIGNER_NUMBER = 1352

startPosition = (1, 1)
origin = (0,0)
destination = (31,39)

nodedt = np.dtype([('wall', np.bool), ('visited', np.bool), ('hops', np.int), ('shortest', np.bool)])
maze = np.ndarray((50,50), dtype=nodedt)

def isWall(coords):
    x, y = coords
    value = (x*x + 3*x + 2*x*y + y + y*y) + DESIGNER_NUMBER
    binaryRepresentation = "{0:b}".format(value)
    return binaryRepresentation.count("1") % 2 != 0

def initMaze():
    it = np.nditer(maze, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        it[0]['wall'] = isWall(it.multi_index)
        it[0]['visited'] = False
        it[0]['hops'] = 1000
        it[0]['shortest'] = False
        it.iternext()

def checkNeighbour(hops, x, y):
    if (x >= 0) and (x < 50) and (y >= 0) and (y < 50) and not maze[x, y]['wall']:
        if maze[x, y]['hops'] > hops + 1:
            maze[x, y]['hops'] = hops + 1

def visitNeighbour(x, y):
    if (x >= 0) and (x < 50) and (y >= 0) and (y < 50) and not maze[x, y]['wall'] and not maze[x,y]['visited']:
        calculateHops((x,y))

def calculateHops(location):
    x, y = location
    hops = maze[x,y]['hops']
    checkNeighbour(hops, x - 1, y)
    checkNeighbour(hops, x + 1, y)
    checkNeighbour(hops, x, y - 1)
    checkNeighbour(hops, x, y + 1)
    maze[x,y]['visited'] = True
    visitNeighbour(x - 1, y)
    visitNeighbour(x + 1, y)
    visitNeighbour(x, y - 1)
    visitNeighbour(x, y + 1)

def lowerHop(x, y, lowestHops, nextNode):
    if maze[x, y]['hops'] < lowestHops:
        lowestHops = maze[x, y]['hops']
        nextNode = (x, y)
    return lowestHops, nextNode

def shortestPath(location, pathLength = 0):
    x, y = location
    maze[x, y]['shortest'] = True
    if maze[x, y]['hops'] == 0:
        return pathLength
    else:
        nextNode = location
        lowestHops = maze[x,y]['hops']
        lowestHops, nextNode = lowerHop(x + 1, y, lowestHops, nextNode)
        lowestHops, nextNode = lowerHop(x - 1, y, lowestHops, nextNode)
        lowestHops, nextNode = lowerHop(x, y - 1, lowestHops, nextNode)
        lowestHops, nextNode = lowerHop(x, y + 1, lowestHops, nextNode)
        return shortestPath(nextNode, pathLength + 1)

def printMaze():
    print('          1         2         3         4')
    print('01234567890123456789012345678901234567890123456789')
    i = 0
    for line in maze[0:]:
        result = []
        for item in line:
            if item['wall']:
                result.append('#')
            elif item['hops'] <= 50:
                result.append(str(item['hops'])[0])
            elif item['shortest']:
                result.append('O')
            elif item['visited']:
                result.append('x')
            else:
                result.append('.')
        print("".join(result), i)
        i += 1
    print('          1         2         3         4')
    print('01234567890123456789012345678901234567890123456789')

if __name__ == '__main__':
    initMaze()

    maze[startPosition[0], startPosition[1]]['hops'] = 0
    calculateHops(startPosition)
    pathLength = shortestPath(destination)
    printMaze()
    print('\nShortest path is length', pathLength)

    atMost50Hops = 0
    nodesVisited = 0
    for node in np.nditer(maze):
        nodesVisited += 1
        if node['hops'] <= 50:
            atMost50Hops += 1

    print ("Of {0} total nodes, {1} are reachable in at most 50 hops:".format(nodesVisited, atMost50Hops))
    print("(10, 9)=", maze[10, 9]['hops'])