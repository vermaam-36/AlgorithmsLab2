import numpy as np

def findIntersection(poly, checker):
    try:
        if(poly[0] == checker[0] or poly[1] == checker[1]):
            return poly
        m_list = [[poly[0], poly[1]], [checker[0], checker[1]]]
        A = np.array(m_list)
        inv_A = np.linalg.inv(A)
        print(inv_A)
        B = np.array([poly[2], checker[2]])
        X = np.linalg.inv(A).dot(B)
        print(X)
        return X
    except:
        return

