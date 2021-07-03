from math import inf

f = open("1_in.txt")
g = open("1_out.txt", "w")
n = int(f.readline().strip())
for i in range (n):                 # pentru fiecare etst din fisierul de intrare
    m = int(f.readline().strip())   # citesc numarul de semiplane
    x_inf = -inf                    # imi setez limitele initiale
    x_sup = inf
    y_inf = - inf
    y_sup = inf
    for j in range(m):              # pentru fiecare semiplan
        list = f.readline().strip().split()
        a = float(list[0])
        b = float(list[1])
        c = float(list[2])
        if a==0:
            if b>0:
                y_sup = min(-c / b, y_sup)      # pentru superior iau minimul
            else:
                y_inf = max(- c/b, y_inf)       # pentru inferior iau maximul
        elif b==0:
            if a >0:
                x_sup = min(- c/a, x_sup)
            else:
                x_inf = max(- c / a, x_inf)

    if x_inf < x_sup and  y_inf < y_sup:        # daca delimitarile formeaza un dreptunghi
        if x_inf==-inf or x_sup==inf or y_inf==-inf or y_sup == inf:    # verific marginirea
            g.write("intersectie nevida, nemarginita\n")
        else:
            g.write("intersectie nevida, marginita\n")
    else:
        g.write("intersectie vida\n")
    print(x_inf, x_sup, y_inf, y_sup)



