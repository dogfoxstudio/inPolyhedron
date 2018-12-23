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
    
def inPolygonxy(pol, x, y):
    pos = False
    for i in range(1, len(pol)):
            x1 = pol[i-1][0]
            y1 = pol[i-1][1]
            x2 = pol[i][0]
            y2 = pol[i][1]
            if ((y1 < y < y2) or (y2 < y < y1)) and x < (y-y1)*(x2-x1)/(y2-y1)+x1:
                pos = not pos
    #print(pos)
    return pos

def inPolygonxz(pol, x, z):
    pos = False
    for i in range(1, len(pol)):
            x1 = pol[i-1][0]
            z1 = pol[i-1][2]
            x2 = pol[i][0]
            z2 = pol[i][2]
            if ((z1 < z < z2) or (z2 < z < z1)) and x < (z-z1)*(x2-x1)/(z2-z1)+x1:
                pos = not pos
    #print(pos)
    return pos

getFigure("polyhedron.db")

def isIn(polygons, x, y, z):
    xy = False
    xz = False
    for pol in polygons:
        xy = xy or inPolygonxy(pol, x, y)
        xz = xz or inPolygonxz(pol, x, z)
        #print(xy)
        #print(xz)
    isin = xz and xy
    return isin

#print(dots)
#print(polygons)

def test(x,y,z):
    return(isIn(polygons ,x,y,z))
    
#print(test(1,1,1))