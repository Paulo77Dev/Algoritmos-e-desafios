x = input().split()
a, b = x
a = int(a)
b = int(b)
original = []
z = []
contador = 0
for i in range (0,a):
    z = input().split()
    x = len(z)
    if x == b:
        list(z)
        original += (z)
for i in range (0,b):
    for i in range (i,a*b,b):
        if contador < a-1:
            print(original[i],end=" ")
            contador += 1
        else:
            contador = 0
            print(original[i],end="")
    print()