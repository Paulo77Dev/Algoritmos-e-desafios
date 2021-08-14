seguidores1 = []
seguidores2 = []
comum = []
john = []
peter = []
lista1 = input()
seguidores1excluidos = []
seguidores2excluidos = []
while lista1 != "fim":
    seguidores1 += [lista1]
    lista1 = input()
lista2 = input()
while lista1 == "fim" and lista2 != "fim":
    seguidores2 += [lista2]
    lista2 = input()
x1 = len(seguidores1)
x2 = len(seguidores2)
for i in range (0,x1):
    for y in range (0,x2):
        if seguidores1[i] == seguidores2[y]:
            comum += [seguidores1[i]]
            seguidores1excluidos += [i]
            seguidores2excluidos += [y]
for i in range (0,x1):
    if i in seguidores1excluidos:
        john = john
    else:
        john += [seguidores1[i]]
for i in range (0,x2):
    if i in seguidores2excluidos:
        peter = peter
    else:
        peter += [seguidores2[i]]
print ("Comum:",comum)
print("John:",john)
print("Peter:",peter)