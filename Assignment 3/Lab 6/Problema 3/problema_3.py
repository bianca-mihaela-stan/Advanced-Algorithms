from sympy.geometry import Triangle, Point

f = open("3_in.txt", "r")
g = open("3_out.txt", "w")

A = [float(x) for x in f.readline().strip().split()]
B = [float(x) for x in f.readline().strip().split()]
C = [float(x) for x in f.readline().strip().split()]

triangle = Triangle(A, B, C)

n = int(f.readline())
for i in range(n):
    query = [float(x) for x in f.readline().strip().split()]
    print(triangle.incenter.distance(query))
    # Verific cu distanta din centrul cercului circumscris.
    if triangle.circumcenter.distance(query) < triangle.circumradius:
        g.write(f"({query[0]}, {query[1]}) - in interior\n")
    elif triangle.circumcenter.distance(query) == triangle.circumradius:
        g.write(f"({query[0]}, {query[1]}) - pe cerc\n")
    else:
        g.write(f"({query[0]}, {query[1]}) - in exterior\n")