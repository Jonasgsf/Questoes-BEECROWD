contador = 0
for i in range(5):
    a = int(input())
    if a % 2 == 0:
        contador += 1
print(f'{contador} valores pares')