a = int(input())
b = int(input())
c = 0
if a > b: 
    c = a 
    a = b 
    b = c
soma = b
for i in range(a,b):
    soma = soma + a
    print(a,end=" + ")
    a = a + 1
print(a,"=",soma)