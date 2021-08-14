numeros = input().split()
x = len(numeros)
numeros = [int(val) for val in numeros]
maior = 0
posicao = 0
for i in range (0,x):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i
print("lista[{}] = {}".format(posicao,maior))