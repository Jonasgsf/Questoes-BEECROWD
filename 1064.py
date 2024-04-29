contador = 0
soma = 0
for i in range(6):
    a = float(input())
    if a > 0:
        contador += 1
        soma += a
print(f'{contador} valores positivos\n{soma / contador:.1f}')