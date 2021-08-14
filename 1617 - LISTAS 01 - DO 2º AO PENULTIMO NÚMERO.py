lista1 =[]
for x in range (0, 20):
  x = x + 1
  lista = input ()
  if x >1 and x < 20:
    lista1 += [lista]
print(" ".join(lista1))