lista1 = []
lista = int(input ())
while lista >= 0:
    lista1 += [lista]
    lista = int(input())
newList = list(reversed(lista1))
print (*newList)