#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

dots = []
polygons = []

def getFigure(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for id in cursor.execute("SELECT x,y,z FROM dots"):
        #print(id)
        dots.append(id)
    #print(dots)

    for id in cursor.execute("SELECT * FROM polygons;"):
        #print(id[1::])
        polygons.append(list(id[1::]))
    for i in range(len(polygons)):
        polygons[i].append(polygons[i][0])
        for j in range(len(polygons[i])):
            polygons[i][j] = dots[polygons[i][j] - 1]
    #print(polygons)
    
def isIn(plg, x, y, z):
    pos = False
    for polygon in polygons:
        pos1 = False
        pos2 = False
        pos3 = False
        #print(len(polygon))
        for i in range(1, len(polygon)):
            x1 = polygon[i-1][0]
            y1 = polygon[i-1][1]
            x2 = polygon[i][0]
            y2 = polygon[i][1]
            if ((y1 < y < y2) or (y2 < y < y1)) and x < (y-y1)*(x2-x1)/(y2-y1)+x1:
                pos1 = not pos1
        print(pos1, "1")
        for i in range(1, len(polygon)):
            x1 = polygon[i-1][0]
            z1 = polygon[i-1][2]
            x2 = polygon[i][0]
            z2 = polygon[i][2]
            if ((z1 < z < z2) or (z2 < z < z1)) and x < (z-z1)*(x2-x1)/(z2-z1)+x1:
                pos2 = not pos2
        print(pos2 ,"2")
        for i in range(1, len(polygon)):
            z1 = polygon[i-1][2]
            y1 = polygon[i-1][1]
            z2 = polygon[i][2]
            y2 = polygon[i][1]
            if ((y1 < y < y2) or (y2 < y < y1)) and z < (y-y1)*(z2-z1)/(y2-y1)+z1:
                pos3 = not pos3
        print(pos3, "3")
        if(pos1 or pos2 or pos3):
            pos = True
        else:
            
            return False
    return pos
            

getFigure("polyhedron.db")

#print(dots)
#print(polygons)

xt1 = 2 # IN
yt1 = 2
zt1 = 2
xt2 = 0 # OUT
yt2 = 0
zt2 = 4
xt3 = 5 # OUT
yt3 = 5
zt3 = 3

print(isIn(polygons, 1,2,1))
