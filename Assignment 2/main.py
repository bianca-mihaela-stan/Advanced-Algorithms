import copy
import math
import random
import matplotlib.pyplot as plt
import time

probabilitati_selectie = []
y = 0
n = 0
N = 0
a =0
b =0
A=0
B=0
C=0
p=0
p_recomb =0
p_mutatie =0
elitist =0
tip_mutatie= 0
best_fitness = 0
fittest = []
l=0
populatie=[]
fit_values = []
populatia_dupa_recombinare =[]
individ_cu_fitness_maxim_din_populatia_curenta = []


# Parseaza input-ul din input.txt.
def parse_input():
    global n, N, a, b, A, B, C, p, p_recomb, p_mutatie, elitist, tip_mutatie, best_fitness, fittest, probabilitati_selectie, y
    f = open("input.txt", "r")
    n=int(f.readline())
    a=float(f.readline())
    b=float(f.readline())
    A=float(f.readline())
    B=float(f.readline())
    C=float(f.readline())
    p=float(f.readline())
    p_recomb=float(f.readline())
    p_mutatie=float(f.readline())
    N=int(f.readline())
    elitist = False
    best_fitness=0

    print("Se foloseste criteriul elitist? 0/1 ")
    optiune = int(input())
    if optiune == 1:
        elitist = True


    tip_mutatie = 0
    print("Ce timp de mutare se foloseste? 0 - mutatie rara, 1 - pentru fiecare gena")
    optiune = int(input())
    if optiune == 1:
        tip_mutatie = 1

# Afiseaza in output.txt datele de intrare primite.
def afisare_input():
    global n, N, a, b, A, B, C, p, p_recomb, p_mutatie, elitist, tip_mutatie, best_fitness, fittest, probabilitati_selectie, y
    g.write("---------------------------------\n")
    g.write("DATELE DE INTRARE\n")
    g.write("---------------------------------\n")
    g.write(f"Dimensiunea populatiei: {n}\n")
    g.write(f"Domeniul de definitie al functiei: [{a},{b}]\n")
    g.write(f"Functia: f(x) = {A}x^2 + {B}x +{C}\n")
    g.write(f"Precizia cu care distretizam intervalul: {p}\n")
    g.write(f"Probabilitatea de recombinare: {p_recomb}\n")
    g.write(f"Probabilitatea de mutatie: {p_mutatie}\n")
    g.write(f"Numarul de etape al algoritmului: {N}\n")
    if elitist:
        g.write("Se tine cont de criteriul elitist.\n")
    else:
        g.write("Nu se tine cont de criteriul elitist.\n")
    if tip_mutatie==0:
        g.write("Se foloseste mutatia rara.\n")
    else:
        g.write("Se foloseste mutatia pentru fiecare gena.\n")


# Gaseste lungimea necesara pentru codificare.
def codificare():
    global l
    l = int(math.log2((b - a)*pow(10, p)))+1

# Genereaza l gene random pentru un individ.
def generare_cromozomi():
    individ=[]
    for i in range(l):
        individ.append(random.randint(0, 1))
    return individ

# Genereaza genele pentru intreabga populatie initiala.
def generare_populatie():
    g.write("Populatia la pasul 1:\n")
    global populatie
    populatie = []
    for i in range(n):
        individ=generare_cromozomi()
        populatie.append(individ)
        g.write(f"X_{i} : {individ}, adica x = {base_2_to_base_10(individ)}, f(x) = {fitness(individ)}\n")

# Transforma individul in baza 2 numarul corespunzator lui in baza 10.
def base_2_to_base_10(individ):
    putere = 1
    nr = 0
    for i in range(len(individ)-1, -1, -1):
        nr+=putere*individ[i]
        putere*=2
    nr= (b-a)/(pow(2,l)-1)*nr+a
    return nr

# Calculeaza fitness-ul unui individ.
def fitness(individ):
    x = base_2_to_base_10(individ)
    return A*pow(x, 2)+B*x + C

# Aplica functia f pe un numar.
def f(x):
    return A*pow(x, 2)+B*x + C

# Cauta intr-o lista list locul lui x prin cautare binara.
def cautare_interval(list, x, left, right):
    if x<=list[left]:
        return left
    elif x>=list[right]:
        return right + 1
    elif left < right:
        mid = int((left+right)/2)
        if list[mid]<=x and list[mid+1]>x:
            return mid+1
        elif list[mid]<=x and list[mid+1]<=x:
            return cautare_interval(list, x, mid+2, right)
        else:
            return cautare_interval(list, x, left, mid-1)

# Face selectia din populatie.
def selectie(populatie):
    global n, N, a, b, A, B, C, p, p_recomb, p_mutatie, elitist, tip_mutatie, best_fitness, fittest, probabilitati_selectie, y, index_individ_cu_fitness_maxim, individ_cu_fitness_maxim_din_populatia_curenta

    if y==1:
        g.write("---------------------------------\n")
        g.write(f"SELECTIA la pasul {y}\n")
        g.write("---------------------------------\n")

    global populatie_intermediara
    populatie_intermediara = []
    indecsi_populatie_intermediara = []
    # F este suma fitness-urilor tuturor indivizilor.
    F=0
    for i in range(len(populatie)):
        F+=fitness(populatie[i])

    if y == 1:
        g.write("Probabilitati de selectie: \n")

    # Calculam probabilitatea de selectie pentru fiecare individ.
    for i in range(len(populatie)):
        probabilitati_selectie.append(fitness(populatie[i])/F)
        if y == 1:
            g.write(f"X_{i} are probabilitate {probabilitati_selectie[i]}.\n")

    # Daca folosim criteriul elitist aleg n-1 indivizi.
    if elitist == True:
        j=1
    else:
        j=0

    # Calculez individul cu fitness maxim pentru:
    # - selectia elitista daca e cazul
    # - sa il afisez in output
    # - sa il pun in grafic
    fitness_maxim = 0
    index_individ_cu_fitness_maxim = []
    for i in range(len(populatie)):
        if fitness_maxim < fitness(populatie[i]):
            fitness_maxim = fitness(populatie[i])
            index_individ_cu_fitness_maxim = i
            individ_cu_fitness_maxim_din_populatia_curenta = copy.deepcopy(populatie[i])
    if best_fitness < fitness_maxim:
        best_fitness = fitness_maxim
        fittest = populatie[index_individ_cu_fitness_maxim]

    fit_values.append(base_2_to_base_10(fittest))

    if elitist == True:
        # indecsi_populatie_intermediara.append(index_individ_cu_fitness_maxim)
        if y == 1:
            g.write(f"X_{index_individ_cu_fitness_maxim} este individul elitist.\n")

    if y == 1:
        g.write("Intervale de selectie: \n")

    # Calculez intervalele de sectie.
    intervale=[]
    for i in range(0, n):
        interval_selectie = 0
        for q in range (0, i+1):
            interval_selectie+=probabilitati_selectie[q]
        intervale.append(interval_selectie)
        if y == 1:
            if i == n-1:
                g.write(f"X_{i} : [{intervale[i - 1]}, 1) \n\n")
            elif i == 0:
                g.write(f"X_{i} : [0, {intervale[i]}), \n")
            else:
                g.write(f"X_{i} : [{intervale[i-1]}, {intervale[i]}), \n")


    while j<n:
        # Generez un numar random intre 0 si 1 si ii caut pozitia in intervalele de selecte.
        x = random.uniform(0, 1)
        poz = cautare_interval(intervale, x, 0, len(intervale)-1)
        if poz > len(populatie)-1:
            poz = -1
        if y == 1:
            g.write(f"S-a generat numarul {x} si a fost incadrat in intervalul {poz}.\n")
        if poz > len(intervale)-1:
            poz = len(intervale)-1
        # Adaug pozitia la indecsii pentru populatia intermediara.
        indecsi_populatie_intermediara.append(poz)
        j+=1

    # Acum creez si populatia intermediara.
    for index in indecsi_populatie_intermediara:
        populatie_intermediara.append((index, populatie[index]))

    if y == 1:
        g.write(f"Dupa selectie: \n")
        for index in indecsi_populatie_intermediara:
            individ = populatie[index]
            if y == 1:
                g.write(f"X_{index} : {individ}, adica x={base_2_to_base_10(individ)}, cu f(x)= {fitness(individ)}\n")

def recombinare():
    if y == 1:
        g.write("---------------------------------\n")
        g.write(f"RECOMBINAREA la pasul {y}\n")
        g.write("---------------------------------\n")

    global populatie_recombinare
    global fara_recombinare
    global populatie_recombinata
    global populatia_dupa_recombinare
    populatie_recombinata=[]
    populatie_recombinare=[]
    fara_recombinare=[]
    populatia_dupa_recombinare=[]

    if y == 1:
        g.write(f"\nProbabilitatea de recombinare este {p_recomb}.\n\n")

    if y == 1:
        g.write("La recombinare participa: \n")

    # Pentru recombinare, pentru fiecare individ generez un numar random de la 0 la 1. Daca acesta e mai mic
    # ca probabilitatea de recombinare, individul participa la recombinare.
    for individ in populatie_intermediara:
        x = random.uniform(0, 1)
        if x < p_recomb:
            populatie_recombinare.append(individ)
            if y == 1:
                g.write(f"X_{individ[0]}: {individ[1]}, adica x = {base_2_to_base_10(individ[1])} cu f(x)= {fitness(individ[1])}\n")
        else:
            fara_recombinare.append(individ[1])

    # Amestec indivizii pentru recombinare.
    random.shuffle(populatie_recombinare)

    i=0
    while i<len(populatie_recombinare) and i+1<len(populatie_recombinare):
        # Daca mai am 3 indivizi ramasi.
        if(i+2== len(populatie_recombinare)-1):
            individ1 = populatie_recombinare[i][1]
            individ2 = populatie_recombinare[i + 1][1]
            individ3 = populatie_recombinare[i + 2][1]
            index_individ1 = populatie_recombinare[i][0]
            index_individ2 = populatie_recombinare[i + 1][0]
            index_individ3 = populatie_recombinare[i + 2][0]
            if y == 1:
                g.write(f"Se recombina: \n")
                g.write(f"X_{index_individ1} adica {individ1} cu \n")
                g.write(f"X_{index_individ2} adica {individ2} cu\n")
                g.write(f"X_{index_individ3} adica {individ3}\n")

            # Generez un punct de rupere.
            punct_rupere = random.randint(0, l)

            if y == 1:
                g.write(f"Punctul de rupere este: {punct_rupere}\n")

            bucata11 = individ1[0:punct_rupere]
            bucata12 = individ1[punct_rupere:]
            bucata21 = individ2[0:punct_rupere]
            bucata22 = individ2[punct_rupere:]
            bucata31 = individ3[0:punct_rupere]
            bucata32 = individ3[punct_rupere:]

            individ1_recombinat = bucata11 + bucata32
            individ2_recombinat = bucata21 + bucata12
            individ3_recombinat = bucata31 + bucata22

            populatie_recombinata.append(individ1_recombinat)
            populatie_recombinata.append(individ2_recombinat)
            populatie_recombinata.append(individ3_recombinat)

            if y == 1:
                g.write("Noii indivizi sunt: \n")
                g.write(f"{individ1_recombinat}\n")
                g.write(f"{individ2_recombinat}\n")
                g.write(f"{individ3_recombinat}\n")

            i += 3
        else:
            # Recombinare cu 2 indivizi.
            individ1 = populatie_recombinare[i][1]
            individ2 = populatie_recombinare[i+1][1]
            index_individ1 = populatie_recombinare[i][0]
            index_individ2 = populatie_recombinare[i+1][0]

            if y == 1:
                g.write(f"Se recombina: \n")
                g.write(f"X_{index_individ1} adica {individ1} cu \n")
                g.write(f"X_{index_individ2} adica {individ2}\n")

            punct_rupere = random.randint(0, l)

            if y == 1:
                g.write(f"Punctul de rupere este: {punct_rupere} \n")

            bucata11 = individ1[0:punct_rupere]
            bucata12 = individ1[punct_rupere:]
            bucata21 = individ2[0:punct_rupere]
            bucata22 = individ2[punct_rupere:]

            individ1_recombinat = bucata11 + bucata22
            individ2_recombinat = bucata21 + bucata12

            populatie_recombinata.append(individ1_recombinat)
            populatie_recombinata.append(individ2_recombinat)

            if y == 1:
                g.write("Noii indivizi sunt: \n")
                g.write(f"{individ1_recombinat}\n")
                g.write(f"{individ2_recombinat}\n")

            i+=2

    # Duypa recombinare voi avea inidvizii recombinati si indivizii care nu au participat la recombinare.
    for i in range(len(populatie_recombinata)):
        populatia_dupa_recombinare.append((i, populatie_recombinata[i]))

    for i in range(len(fara_recombinare)):
        populatia_dupa_recombinare.append((i+len(populatie_recombinata), fara_recombinare[i]))
    if y == 1:
        g.write("\nPopulatia dupa recombinare este:\n")
        for individ in populatia_dupa_recombinare:
            g.write(f"Y_{individ[0]}: {individ[1]}, adica x = {base_2_to_base_10(individ[1])} f(x) = {fitness(individ[1])}\n")

def mutatie_rara():
    if y == 1:
        g.write("----------------------------------\n")
        g.write(f"MUTATIA RARA pentru pasul {y}\n")
        g.write("----------------------------------\n")

        g.write(f"\nProbabilitatea de mutatie in mutatia rara a fost: {p_mutatie}")

    # Pentru fiecare individ am generat un numar random intre 0 si 1. Daca acesta e mai mic ca
    # probabilitatea de mutatie vom efectua o mutatie pe el. Generam o alta pozitie random si
    # inversam acel bit din individ.
    for individ in populatia_dupa_recombinare:
        x = random.uniform(0, 1)
        if x < p_mutatie:
            poz = random.randint(0, len(individ[1])-1)
            individ[1][poz]=int(not (individ[1][poz]))
            if y == 1:
                g.write(f"Pentru Y_{individ[0]} se modifica cromozomul de pe pozitia {poz}.\n")
    if y == 1:
        g.write("\nPopulatia dupa mutatie:\n")
        for individ in populatia_dupa_recombinare:
            g.write(f"Y_{individ[0]}: {individ[1]}, adica x = {base_2_to_base_10(individ[1])} f(x) = {fitness(individ[1])}\n")

def mutatie_normala():
    if y == 1:
        g.write("----------------------------------\n")
        g.write(f"MUTATIA PENTRU FIECARE GENA pentru pasul {y}\n")
        g.write("----------------------------------\n")

        g.write(f"\nProbabilitatea de mutatie in mutatia pe fiecare gena a fost: {p_mutatie}")

    # Pentru fiecare bit din fiecare individ generez un numar random de la 0 la 1. Daca acesta este mai mic ca
    # probabilitatea de mutatie inversam acel bit.
    for individ in populatia_dupa_recombinare:
        for poz in range(len(individ[1])):
            x = random.uniform(0,1)
            if x < p_mutatie:
                individ[1][poz] = int(not(individ[1][poz]))
                if y == 1:
                    g.write(f"Pentru Y_{individ[0]} se modifica cromozomul de pe pozitia {poz}.\n")

    if y == 1:
        g.write("Populatia dupa mutatie:\n")
        for individ in populatia_dupa_recombinare:
            g.write(f"Y_{individ[0]}: {individ[1]}, adica x = {base_2_to_base_10(individ[1])} f(x) = {fitness(individ[1])}\n")

def mutatii():
    # Apelez mutatia corespunzatoare in functie de alegerea utilizatorului.
    if tip_mutatie==0:
        mutatie_rara()
    else:
        mutatie_normala()

def plot():
    # Fac 2 grafice:
    # - unul cu evolutia populatiei
    # - unul cu evolutia maximului
    Ox = []
    Oy = []
    Oxy = []
    for individ in populatie:
        Oxy.append((base_2_to_base_10(individ), fitness(individ)))

    sorted(Oxy, key=lambda x: x[0])
    for elem in Oxy:
        Ox.append(elem[0])
        Oy.append(elem[1])

    valori = [f(x) for x in list(fit_values)]
    Ox1 = Ox
    Oy1 = Oy
    Ox2 = list(fit_values)
    Oy2 = valori


    plt.subplot(1, 2, 1)
    plt.scatter(Ox1, Oy1)
    plt.xlabel("individuals from current population")
    plt.ylabel("fitness of individuals from current population")
    plt.subplots_adjust(wspace = 1)


    plt.subplot(1, 2, 2)
    plt.scatter(Ox2, Oy2)
    plt.xlabel("fittest individuals across population")
    plt.ylabel("fitness of fittest individuals across populations")


    plt.show()

    time.sleep(1)


def evolutia_maximului():
    g.write("\nEvolutia maximului:\n")
    valori = [f(x) for x in fit_values]
    for value in valori:
        g.write(f"{value}\n")

g = open("output.txt", "w")
probabilitati_selectie = []
random.seed()
parse_input()
afisare_input()
codificare()
generare_populatie()
y=1
while y<= N:
    plot()
    selectie(populatie)
    recombinare()
    mutatii()
    populatie = []
    for individ in populatia_dupa_recombinare:
        populatie.append(individ[1])
    if elitist==True:
        populatie.append(individ_cu_fitness_maxim_din_populatia_curenta)
    y+=1

print(fit_values)
evolutia_maximului()