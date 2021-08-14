frase = str(input())
x = frase.split()
unindo = "".join(x)
lista = list(unindo)
novalista = list(reversed(unindo))
if lista == novalista:
    print ("'{}' eh palindromo".format(frase))
else:
    print ("'{}' nao eh palindromo".format(frase))