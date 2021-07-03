f = open("2_in.txt", "r")
g = open("2_out.txt", "w")
nr_poligoane = int(f.readline())

# Pentru fiecare poligon:
for i in range (nr_poligoane):
    g.write(f"Poligonul {i+1}:\n")
    n = int(f.readline())
    poligon = []
    leftest = None
    shortest = None
    for i in range(n):
        line=f.readline().strip().split(" ")
        x = float(line[0])
        y = float(line[1])
        poligon.append((x, y))
        if leftest == None:
            leftest = i
        elif x < poligon[leftest][0]:
            leftest = i
        if shortest == None:
            shortest = i
        elif x < poligon[shortest][1]:
            shortest = i

    # Verific daca este x-monoton.
    current = poligon[leftest]
    next = poligon[(leftest + 1) % n]
    i = (leftest + 1) % n
    ok=True
    # initial ar trebui sa creasca si nu sa scada
    crestere = True
    scadere = False
    monoton = True
    while ok:
        if next[0] == current[0]:
            monoton = False
        elif crestere == True:
            # daca scade inseamna ca ne ducem inapoi
            if current[0] > next[0]:
                crestere = False
                scadere = True
        elif scadere == True:
            # daca a scazut si acum iar creste inseamna ca nu e monoton
            if current[0] < next[0]:
                monoton = False

        if monoton == False:
            g.write("nu este x-monoton\n")
            ok = False
        else:
            current = next
            # trebuie sa fac inconjurul, deci ma opresc cand ajung se unde
            # am plecat
            i = (i + 1) % n
            if i == leftest:
                ok = False
            next = poligon[i]
    if monoton==True:
        g.write("este x-monoton\n")


    # Verific daca e y-monoton.
    current = poligon[shortest]
    next = poligon[(shortest + 1) % n]
    i = (shortest + 1) % n
    ok = True
    crestere = True
    scadere = False
    monoton = True
    while ok:
        if next[1] == current[1]:
            monoton = False
        elif crestere == True:
            if current[1] > next[1]:
                crestere = False
                scadere = True
        elif scadere == True:
            if current[1] < next[1]:
                monoton = False

        if monoton == False:
            g.write("nu este y-monoton\n")
            ok = False
        else:
            current = next
            i = (i + 1) % n
            if i == shortest:
                ok = False
            next = poligon[i]

    if monoton==True:
        g.write("este y-monoton\n\n")


#
# # Citesc query-urile si apelez functia care sa le pozitioneze.
# m = int(f.readline())
# # print(m)
# for i in range(m):
#     line = f.readline().strip().split(" ")
#     # print(line)
#     x = float(line[0])
#     y = float(line[1])
#     query = (x, y)
#     # print(query)
#
#     poz_relativ_la_polign(query, poligon)
