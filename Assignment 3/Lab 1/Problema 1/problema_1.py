from geompreds import orient2d

f = open("1.in", "r")
g = open("1.out", "w")
n = int(f.readline())
for i in range (n):
    line1=f.readline().strip().split(" ")
    line2 = f.readline().strip().split(" ")
    line3 = f.readline().strip().split(" ")
    x_1 = float(line1[0])
    y_1 = float(line1[1])
    x_2 = float(line2[0])
    y_2 = float(line2[1])
    x_3 = float(line3[0])
    y_3 = float(line3[1])

    eps = 0.000001

    if orient2d((x_1, y_1), (x_2, y_2), (x_3, y_3)) > -eps and orient2d((x_1, y_1), (x_2, y_2), (x_3, y_3)) < eps:
        g.write("coliniare\n")
    elif orient2d((x_1, y_1), (x_2, y_2), (x_3, y_3)) >= eps:
        g.write("stanga\n")
    else:
        g.write("dreapta\n")