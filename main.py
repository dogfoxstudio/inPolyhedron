#!/usr/bin/env python3
# -*- coding: utf-8 -*-

points = [[0,0,0],\
         [3,0,0],\
         [0,6,0],\
         [4,3,0],\
         [1,1,3],\
         [3,0,3],\
         [0,4,3],\
         [4,3,4],\
        ]


polygons = [
        [points[0], points[1], points[3], points[2], points[0]],\
        [points[0], points[4], points[5], points[1], points[0]],\
        [points[1], points[5], points[7], points[3], points[1]],\
        [points[3], points[7], points[6], points[2], points[3]],\
        [points[0], points[4], points[6], points[2], points[0]],\
        [points[4], points[5], points[7], points[6], points[4]]\
        ]
        
xt1 = 2 # IN
yt1 = 2
zt1 = 2
xt2 = 0 # OUT
yt2 = 0
zt2 = 4
xt3 = 5 # OUT
yt3 = 5
zt3 = 3

# луч параллелен OY следовательно создаем проекции на плоскость OXZ

def planeOnOXY():
    for i in range(len(polygons)):
        for j in range(len(polygons[i])):
            polygons[i][j][2] = 0
            
planeOnOXY()
for polygon in polygons:
    print(polygon)
def isIn(x, y):
    for polygon in polygons:
        pos = False
        #print(len(polygon))
        for i in range(1, len(polygon)):
            x1 = polygon[i-1][0]
            y1 = polygon[i-1][1]
            x2 = polygon[i][0]
            y2 = polygon[i][1]
            if ((y1 < y < y2) or (y2 < y < y1)) and x < (y-y1)*(x2-x1)/(y2-y1)+x1:
                pos = not pos
        print(pos)
