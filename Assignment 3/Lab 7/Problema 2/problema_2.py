from math import inf

f = open("2_in.txt")
g = open("2_out.txt", "w")

n = int(f.readline().strip())
for i in range(n):                  # pentru fiecare test din input
    g.write(f"exemplul {i + 1}:\n")
    list = f.readline().strip().split()
    q_x = float(list[0])            # citesc coordonatele punctului
    q_y = float(list[1])

    m = int(f.readline().strip())
    x_inf = -inf                    # imi setez limitele initiale
    x_sup = inf
    y_inf = -inf
    y_sup = inf
    for j in range (m):             # pentru fiecare semiplan
        list = f.readline().strip().split()
        a = float(list[0])
        b = float(list[1])
        c = float(list[2])
        if a==0:
            if b>0:
                if q_y<= -c/b:              # consider doar semiplanurile care includ punctul meu
                    y_sup = min(-c / b, y_sup)
            else:
                if q_y >= -c/b:
                    y_inf = max(- c / b, y_inf)
        elif b==0:
            if a > 0:
                if q_x <= -c/a:
                    x_sup = min(- c / a, x_sup)
            else:
                if q_x >= -c/a:
                    x_inf = max(- c / a, x_inf)
    if x_inf<= q_x <= x_sup and y_inf <= q_y <= y_sup and x_inf!=-inf and x_sup!=inf and y_inf !=-inf and y_sup!= inf:  # daca se formeaza un dreptunghi cu punctul in el
        g.write("(a) exista un dreptungi cu proprietatea ceruta\n")
        g.write(f"(b) aria minima este {(x_sup-x_inf)*(y_sup-y_inf)}\n")
    else:
        g.write("(a) nu exista un dreptungi cu proprietatea ceruta\n")


