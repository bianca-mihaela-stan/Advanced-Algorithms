f = open("input.txt")
n = int(f.readline().split())
semiplane = []
for i in range (n):
    a = float(f.readline().strip())
    b = float(f.readline().strip())
    c = float(f.readline().strip())
    semiplane.append((a,b,c))