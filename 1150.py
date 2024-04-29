x = int(input())
z = int(input())
qtd_valores = 1
soma = x
consecutivo = 1
while z <= x:
    z = int(input())

while soma < z:

    soma += (x + qtd_valores)
    qtd_valores += 1

print(qtd_valores)
