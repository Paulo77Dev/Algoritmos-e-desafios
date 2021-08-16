lista1 = []
lista = float(input ())
soma = 0
valor = 0
dp = 0
while lista >= 0:
    lista1 += [lista]
    soma += lista
    lista = float(input())
x = int(len(lista1))
media = soma/x
for i in range (0,x):
    valor = lista1[i]
    dp = dp+((valor-media)**2)
desviopadrao = (dp/x)**0.5
print ("Media: {0:.2f}".format(media))
print ("Desvio Padrao: {0:.2f}".format(desviopadrao))