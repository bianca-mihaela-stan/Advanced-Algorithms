import random
from math import inf, floor

from geompreds import orient2d
from shapely.geometry import LineString, Point
poz = -1


def test_de_orientare(A, B, C):
    eps = 0.00001               # Iau un epsilon pentru numerele reale.
    x = orient2d((A[0], A[1]), (B[0], B[1]), (C[0], C[1]))
    if -eps < x < eps:
        return 0
    elif x >= eps:
        return 1 # stanga
    else:
        return 2 # dreapta


def find_martor(query, poligon):
    global rightest, tallest
    # Martorul il iau la dreapta celui mai din dreapta punct din poligon
    # si mai sus de cel mai sus punct din poligon ca sa ma asigur ca
    # nu e in poligon.
    random.seed()
    ok=True
    # Caut martori pana gasesc unul care sa nu fie coliniar cu PQ,
    # unde P e orice punct ce defineste poligonul si Q este punctul de query.
    while ok:
        ok=False
        x = random.randint(rightest-1000, rightest)
        y = random.randint(tallest, tallest + 1000)
        for point in poligon:
            if test_de_orientare((x,y), query, point) == 0:
                ok = True
        if ok == False:
            return (x,y)


def poz_relativ_la_polign(query, poligon):
    print(f"for query {query}")
    for i in range(len(poligon)-1):
        A = poligon[i]
        B = poligon[i+1]
        C = query
        # daca e coliniar cu una din laturi
        if test_de_orientare(A, B, C)==0:
            # Ma uit cum sunt pozitionate punctele A si B si in functie de asta
            # vad daca C e intre ele sau nu
            if A[0] < B[0]:
                if A[0] <= C[0] <= B[0]:
                    g.write(f"({query[0]},{query[1]}) - pe una din laturi\n")
                    return
            elif B[0] < A[0]:
                if B[0] <= C[0] <= A[0]:
                    g.write(f"({query[0]},{query[1]}) - pe una din laturi\n")
                    return
            else:
                if A[1] < B[1]:
                    if A[1] <= C[1] <= B[1]:
                        g.write(f"({query[0]},{query[1]}) - pe una din laturi\n")
                        return
                elif B[1] < A[1]:
                    if B[1] <= C[1] <= A[1]:
                        g.write(f"({query[0]},{query[1]}) - pe una din laturi\n")
                        return
                else:
                    g.write(f"({query[0]},{query[1]}) - pe una din laturi\n")
                    return

    # Imi caut un punct martor in afara poligonului.
    martor_point = find_martor(query, poligon)
    print(f"martor point {martor_point}")

    # Si numar intersectiile.
    nr_intersections = 0
    for i in range(len(poligon) - 1):
        A = poligon[i]
        B = poligon[i + 1]

        line1 = LineString([A, B])
        line2 = LineString([query, martor_point])
        point_of_intersection = line1.intersects(line2)
        if point_of_intersection == True:
            nr_intersections+=1

    print(f"nr intersections {nr_intersections}")
    if nr_intersections%2==0:
        g.write(f"({query[0]},{query[1]}) - exterior\n")
    else:
        g.write(f"({query[0]},{query[1]}) - interior\n")


f = open("1_in.txt", "r")
g = open("1_out.txt", "w")
n = int(f.readline())
poligon = []
leftest = None                   # indicele celui mai din stanga
                                            # punct din poligon
rightest = None                  # indicele celui mai din dreapta
                                            # punct din poligon
tallest = None                  # indicele celui mai de sus
                                            # punct din poligon
shortest = None                  # indicele celui mai de jos
                                            # punct din poligon

for i in range (n):                         # citesc numerele
    line=f.readline().strip().split(" ")
    x = float(line[0])
    y = float(line[1])
    poligon.append((x, y))
    if leftest == None:
        leftest = i
    elif x < poligon[leftest][0]:
        leftest = i
    if rightest == None:
        rightest = i
    elif x > poligon[rightest][0]:
        rightest = i
    if tallest == None:
        tallest = i
    elif x > poligon[tallest][1]:
        tallest = i
    if shortest == None:
        shortest = i
    elif x < poligon[shortest][1]:
        shortest = i

# Citesc query-urile si apelez functia care sa le pozitioneze.
m = int(f.readline())
# print(m)
for i in range(m):
    line = f.readline().strip().split(" ")
    # print(line)
    x = float(line[0])
    y = float(line[1])
    query = (x, y)
    # print(query)

    poz_relativ_la_polign(query, poligon)
