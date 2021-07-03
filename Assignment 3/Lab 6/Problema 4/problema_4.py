from sympy.geometry import Triangle, Point

f = open("4_in.txt", "r")
g = open("4_out.txt", "w")

A = [float(x) for x in f.readline().strip().split()]
B = [float(x) for x in f.readline().strip().split()]
C = [float(x) for x in f.readline().strip().split()]

triangle = Triangle(A, B, C)

# Aici nu am avut inpurt, asa ca am luat input-ul de la
# exercitiul 3 si am schimbat punctul D cu fiecare din valorile de acolo.
n = int(f.readline())
for i in range(n):
    D = [float(x) for x in f.readline().strip().split()]
    g.write(f"In patrulaterul ABCD ({A}, {B}, {C}, {D}):\n")
    # Verific cu distanta din centrul cercului circumscris.
    if triangle.circumcenter.distance(D) < triangle.circumradius:
        g.write(f"muchia AC ({A}, {C}) este ilegala\n")
        g.write(f"muchia AC ({A}, {C}) este legala\n\n")
    elif triangle.circumcenter.distance(D) == triangle.circumradius:
        g.write(f"muchia AC ({A}, {C}) este legala\n")
        g.write(f"muchia BD ({B}, {D}) este legala\n\n")
        continue
    else:
        g.write(f"muchia AC ({A}, {C}) este legala\n")
        g.write(f"muchia BD ({B}, {D}) este ilegala\n\n")