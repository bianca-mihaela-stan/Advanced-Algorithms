from geompreds import orient2d

poz = -1


def binary_search(arr, low, high, x):
    # Returneaza cel mai din creapta punct <= x. Compararea se face dupa axa Ox.
    global poz
    if low <= high:
        mid = (low+high)//2
        if arr[mid][0] == x[0]:
            poz = mid
            binary_search(arr, mid+1, high, x)
        elif arr[mid][0] < x[0]:
            if poz < mid:
                poz = mid
            binary_search(arr, mid+1, high, x)
        else:
            binary_search(arr, low, mid-1, x)


def incadrare(arr, x):
    global poz
    poz = -1

    # binary_search modifica poz astfel incat sa fie indexul punctului cu cel mai mare x
    # <= ca x-ul punctului de query
    binary_search(arr, 0, len(arr)-1, x)
    pos = poz

    # Daca acest numar e chiar ultimul
    if pos == len(arr)-1:
        if arr[pos][0] == x[0]:     # Verific daca si valoarea de dinaintea lui e egala.
            pos -= 1
        else:                       # Daca nu, inseamna ca punctul de query se afla in afara
                                    # intervalului [ cel_mai_din_stanga_punct, cel_mai_din_dreapta_punct ]
            g.write("outside\n")
            return
    return pos



def test_de_orientare(A, B, C):
    eps = 0.00001               # Iau un epsilon pentru numerele reale.
    x = orient2d((A[0], A[1]), (B[0], B[1]), (C[0], C[1]))
    if -eps < x < eps:
        return 0
    elif x >= eps:
        return 1 # stanga
    else:
        return 2 # dreapta


def poz_relativ_la_polign(query, frontiera_inferioara, frontiera_superioara):

    # Incadrez punctul intr-o latura a poligonului.
    stanga = incadrare(frontiera_inferioara, query)
    dreapta = stanga + 1

    # Fac testul de orientare.
    test_frontiera_inferioara = test_de_orientare(frontiera_inferioara[stanga], frontiera_inferioara[dreapta], query)

    # La prima faza a testului, daca iese "inside", fac si al 2-lea test ca sa fiu sigura.
    if test_frontiera_inferioara == 2:
        g.write("outside\n")
    elif test_frontiera_inferioara == 0:
        if frontiera_inferioara[stanga][0] <= query[0] <= frontiera_inferioara[dreapta][0]:
            g.write("on edge\n")
    else:
        # Al doilea test, pe frontiera superioara.

        stanga = incadrare(frontiera_superioara, query)
        dreapta = stanga + 1

        test_frontiera_superioara = test_de_orientare(frontiera_superioara[stanga], frontiera_superioara[dreapta], query)

        if test_frontiera_superioara == 2:
            g.write("inside\n")
        elif test_frontiera_superioara == 0:
            if frontiera_superioara[stanga][0] <= query[0] <= frontiera_superioara[dreapta][0]:
                g.write("on edge\n")
        else:
            g.write("outside\n")


f = open("3.in", "r")
g = open("3.out", "w")
n = int(f.readline())
poligon = []
cel_mai_din_stanga = None                   # indicele celui mai din stanga
                                            # punct din poligon
cel_mai_din_dreapta = None                  # indicele celui mai din dreapta
                                            # punct din poligon


for i in range (n):                         # citesc numerele
    line=f.readline().strip().split(" ")
    x = float(line[0])
    y = float(line[1])
    poligon.append((x, y))
    if cel_mai_din_stanga == None:
        cel_mai_din_stanga = i
    elif x < poligon[cel_mai_din_stanga][0]:
        cel_mai_din_stanga = i
    if cel_mai_din_dreapta == None:
        cel_mai_din_dreapta = i
    elif x > poligon[cel_mai_din_dreapta][0]:
        cel_mai_din_dreapta = i


# Pun punctele in frontierele corespunzatoare.
frontiera_inferioara = [poligon[cel_mai_din_stanga]]
frontiera_superioara = []

i=cel_mai_din_stanga + 1
ok = True
while ok:
    if i < cel_mai_din_dreapta:
        frontiera_inferioara.append(poligon[i])
    else:
        frontiera_superioara.append(poligon[i])
    if i == cel_mai_din_dreapta:
        frontiera_inferioara.append(poligon[i])

    i = (i + 1) % n
    if i == cel_mai_din_stanga:
        ok = False
frontiera_superioara.append(poligon[cel_mai_din_stanga])

# O inversez pe cea superioara ca sa fac acelasi binary search si pe ea.
# O sa tin cont de acest reverse cand fac testul de orientare.
frontiera_superioara.reverse()


# Citesc query-urile si apelez functia care sa le pozitioneze.
m = int(f.readline())
for i in range(m):
    line=f.readline().strip().split(" ")
    x = float(line[0])
    y = float(line[1])
    query = (x, y)

    poz_relativ_la_polign(query, frontiera_inferioara, frontiera_superioara)
