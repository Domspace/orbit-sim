from math import sqrt


def get_distance(v1, v2):
    return sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)


def get_diff(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(v2[i]-v1[i])
    return v
