"""
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
"""

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

points = [[0,0,0],\
         [10,0,0],\
         [0,10,0],\
         [0,0,5]\
         ]     
         #костыль чтобы замкнуть многоугольник
polygons = [
        [points[0], points[1], points[2], points[0]],\
        [points[0], points[2], points[3], points[0]],\
        [points[0], points[1], points[3], points[0]],\
        [points[1], points[2], points[3], points[1]]\
        ]
        


print(isIn(polygons, 1,2,1))
