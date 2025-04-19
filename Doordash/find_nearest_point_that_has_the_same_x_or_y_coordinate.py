'''

This is a simplified versino of the one that we had the other day

Find the nearest point that has the same x or y coordinate

points[i] = [ai, bi]

x =3 , y = 4

These 2 cases here
x = 3 : [[3, 1]]
y = 4 case : [[2, 4], [4, 4]]

[3, 1]:
  manhattanDistance = 3 -3 + 4 -1 = 3
[2, 4]:
    dist = 3 - 2 + 4 -4 = 1

[4, 4]
    dist = 4 - 4 + 4 -3 =1
deltaX = 0
  '''
from collections import defaultdict
from typing import List

'''
This question is not built complete yet here 
'''


def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    xMap = defaultdict(list)
    yMap = defaultdict(list)

    for index in range(len(points)):
        point = points[index]
        pointX, pointY = point
        if x == pointX:
            xMap[x].append((pointX,pointY, index))
        if y == pointY:
            yMap[y].append((pointX, pointY, index))
    print(xMap)
    minDist = float('inf')
    res = -1
    for item in xMap[x]:
        print(item)
        x2, y2, index = item
        dist = abs(x - x2) + abs(y- y2)
        if dist < minDist:
            minDist = dist
            res = index

    # do the same for the y axis here
    for item in yMap[y]:
        print(item)
        x2, y2, index = item
        dist = abs(x - x2) + abs(y- y2)
        if dist < minDist:
            minDist = dist
            res = index

    print(res)

nearestValidPoint(3, 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]])



