from geompreds import orient2d

f = open("2.in", "r")
g = open("2.out", "w")
n = int(f.readline())
puncte = []
cel_mai_din_stanga = None                   # indicele celui mai din stanga
                                            # element
for i in range (n):                         # citesc numerele
    line=f.readline().strip().split(" ")
    x = float(line[0])
    y = float(line[1])
    puncte.append((x, y))
    if cel_mai_din_stanga == None:
        cel_mai_din_stanga = i
    elif x < puncte[cel_mai_din_stanga][0]:
        cel_mai_din_stanga = i

i = cel_mai_din_stanga
acoperire = [puncte[cel_mai_din_stanga]]    # cel mai din stanga sigur e in acoperire

eps = 0.00001                               # imi iau un epsilon pentru numerele reale

ok = True                                   # ok e True cand timp nu am terminat facut
                                            # inconjurul poligonul
while ok:
    eliminare = True
    while eliminare == True and len(acoperire) >= 3:    # verific ca virajul  pentru ultimele
                                                        # 3 puncte din acoperire sa fie la dreapta
                                                        # pana cand ori nu mai am destul elemente
                                                        # ori ultimele 3 puncte sunt okay si nu e nevoie
                                                        # sa elimin nimic
        last = acoperire[-1]
        middle = acoperire[-2]
        first = acoperire[-3]
        if orient2d((first[0], first[1]), (middle[0], middle[1]), (last[0], last[1])) < eps:
            acoperire.remove(middle)
            eliminare = True
        else:
            eliminare = False

    i = (i+1)%n                         # trec la urmatorul element, dar prin modulo n
    if i == cel_mai_din_stanga:         # cand ajung inapoi de und ea m pornit ma opresc
        ok = False
    else:
        acoperire.append(puncte[i])     # altfel mai adaug un punct

for elem in acoperire:
    g.write(f"{elem[0]} {elem[1]}\n")