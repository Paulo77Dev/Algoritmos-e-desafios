nomecompleto = str(input())
nomecompleto = nomecompleto.upper()
x = nomecompleto.split()
lista = list(x)
ultima = len(lista)-1
if ultima != 0:
    print (lista[ultima],end=", ")
if ultima == 0:
    print (lista[ultima],end=".")
for i in range (0,ultima):
    lista[i] = list(lista[i])
    porletra = lista[i]
    if i != ultima-1:
        print (porletra[0],end=". ")
    if i == ultima-1:
        print (porletra[0]+".")