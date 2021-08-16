html = str(input())
x = len(html)
z = 0
texto = []
for i in range (0,x):
    if z == 0:
        if "<" in html[i]:
            z = 1
        else:
            texto += (html[i])
    if z == 1:
        if ">" in html[i]:
            z = 0
unindo = "".join(texto)
print(unindo)