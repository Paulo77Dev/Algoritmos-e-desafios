par = 0
impar = 0
total = 0
soma = 0
media = 0
while True:
  x=int(input())
  if x==0:
      break
  if x%2==0:
      par=par+1
  else:
      impar=impar+1
  soma=soma+x
  total=impar+par
  if total:= 0:
    media=soma/total
    print("Pares: ",par,"valor(es)")
    print("Ipares: ",impar,"valor(es)")
    print("Media: {:.2f}".format(media))
