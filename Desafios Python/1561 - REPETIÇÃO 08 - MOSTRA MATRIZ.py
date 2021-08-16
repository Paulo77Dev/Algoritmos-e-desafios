a = int(input())
b = int(input())
c = a * b
n = 0
d = b
for i in range(1,c+1):
    b = b - 1
    n = n + 1
    if b > 0:
        print(n,end=" ")
    if b == 0:
        print(n)
        b = d