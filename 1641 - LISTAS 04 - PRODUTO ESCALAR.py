coluna1 = []
coluna2 = []
lista1 = int(input())
soma = 0
while lista1 >= 0:
    coluna1 += [lista1]
    lista1 = int(input())
lista2 = int(input())
while lista1 < 0 and lista2 >=0:
    coluna2 += [lista2]
    lista2 = int(input())
x1 = len(coluna1)
x2 = len(coluna2)
if x1 >= x2:
    x = x2
if x1 < x2:
    x = x1
for i in range (0,x):
    mult = (coluna1[i])*(coluna2[i])
    soma = soma + mult
print ("Produto Escalar:",soma)