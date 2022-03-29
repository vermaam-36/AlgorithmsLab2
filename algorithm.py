from operator import truediv
import numpy as np
import line_intersection

def check_inside(polygon, st_pt):
    horizantal_line= {1, 0, st_pt[0]}
    
    #Format: 0:up, 1:down, 2:left, 3:right
    intersections= 0

    for i in range(0, len(polygon)):
        point1=polygon[i]
        if(i != len(polygon)):
            point2=polygon[i+1]
        else:
            point2=polygon[0]
        
        polygon_line= create_line(point1, point2)
        intersection_point=line_intersection.findIntersection()

        if(intersection_point == None):
            continue
        if(intersection_point == st_pt):
            return True

        intersections+=1
        
    if(intersections%2 == 1):
        return True

    return False


def create_line(pt1, pt2):

    x1 = pt1[0]
    y1 = pt1[1]

    x2 = pt2[0]
    y2 = pt2[1]

    a = y2 - y1
    b = x2 - x1

    c = (a * x1) + (b * y1)
    return np.array([a, b, c])
