a = int(input())
n = 0
primo = 0
for c in range(0,a):
    n = n+1
    x = 0
    total = 0
    for i in range(1,n):
        x = x + 1
        if n%x==0:
            total = total + 1
    if total == 1:
        primo = primo + 1
print("Existe(m)",primo,"numero(s) primo(s) entre 1 e",a)