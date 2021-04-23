from collections import OrderedDict
from math import inf

import numpy as np
from geompreds import orient2d
from functools import cmp_to_key
from scipy.spatial import ConvexHull

def test_de_orientare(A, B, C):
    eps = 0.00001               # Iau un epsilon pentru numerele reale.
    x = orient2d((A[0], A[1]), (B[0], B[1]), (C[0], C[1]))
    if -eps < x < eps:
        return 0
    elif x >= eps:
        return 1 # stanga
    else:
        return 2 # dreapta

def dist (a, b):
    return (a[1]-b[1])**2 + (a[0]-b[0])**2


def step_1(points):
    """
    Calculates the convex hull based on a list of points,
    :param points: [(float, float)]
    :return: [(float, float)]
    """
    ch = ConvexHull(np.array(points))

    convex_hull = [points[x] for x in ch.vertices]

    return convex_hull


def step_2(points, tsp):
    """
    Finds the closest edge in tsp to the points that are not in tsp.
    :param points: [(float, float)] - the list of input points
    :param tsp: [(float, float)] - current tsp computed
    :return: {(int, int): [(float, float)]} - dictionary that maps points to corresponding edges in tsp
    """
    dict_edge_to_point = {}
    for node in points:
        # For each node not in tsp finds the "closest" edge.
        if node not in tsp:
            minn = inf
            pair = None
            for i in range(len(tsp)):
                # Makes the pair (i, j), which are 2 successive points in tsp.
                j = None    
                if i == len(tsp) - 1:
                    j = 0
                else:
                    j = i + 1
                
                p1 = tsp[i]
                p2 = tsp[j]
                if dist(p1, node) + dist(node, p2) - dist(p1, p2) < minn:
                    minn = dist(p1, node) + dist(node, p2) - dist(p1, p2)
                    pair = (i, j)
            if pair not in dict_edge_to_point.keys():
                dict_edge_to_point[pair] = [node]
            else:
                dict_edge_to_point[pair].append(node)

    return dict_edge_to_point

def step_3(dict_edge_to_point, tsp):
    """
    Only adds to tsp the "closest" point to each edge.
    :param dict_edge_to_point: {(int, int): [(float, float)]} - dictionary that maps points to corresponding edges in tsp
    :param ch: 
    :return: 
    """
    list = []
    for pair in dict_edge_to_point.keys():
        # Finds the "closest" point to current edge.
        minn = inf
        nod_minn = None
        for node in dict_edge_to_point[pair]:
            raport = (dist(tsp[pair[0]], node) + dist(node, tsp[pair[1]])) / dist(tsp[pair[0]], tsp[pair[1]])
            if raport < minn:
                minn = raport
                nod_minn = node
        
        # List of tuples: (position where node should be inserted, node)
        list.append((pair[0]+1, nod_minn))

    # We sort the list by the position of insertion so that we can keep
    # track of the changing length of tsp.
    list.sort(key=lambda x : x[0])

    nr_inserted = 0
    for elem in list:
        tsp.insert(elem[0]+nr_inserted, elem[1])
        nr_inserted+=1

    return tsp

def main():
    f = open("4.in", "r")
    g = open("4.out", "w")
    n = int(f.readline())
    points = []

    # Reading input points.
    for i in range (n):
        line=f.readline().strip().split(" ")
        x = float(line[0])
        y = float(line[1])
        points.append((x, y))

    # We perform step_1 only once.
    tsp = step_1(points)

    # We perform steps 2 and 3 until all nodes are in tsp.
    while len(tsp)< len(points):
        dict = step_2(points, tsp)
        ch = step_3(dict, tsp)

    # The nodes might be a permutation of official nodes in result.
    for node in tsp:
        g.write(f"{node[0]} {node[1]}\n")

if __name__ == "__main__":
    main()