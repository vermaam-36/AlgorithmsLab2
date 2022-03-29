import numpy as np

def check_inside(polygon, st_pt):
    


def create_line(pt1, pt2):

    x1 = pt1[0]
    y1 = pt1[1]

    x2 = pt2[0]
    y2 = pt2[1]

    a = y2 - y1
    b = x2 - x1

    c = (a * x1) + (b * y1)
    return np.array([a, b, c])
