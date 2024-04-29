n = int(input())
letra = input().upper
matriz = []

for i in range(12):
    linha_matriz = []
    for j in range(12):
        linha_matriz.append(float(input()))
    matriz.append(linha_matriz)
    
soma = 0
for i in range(12):
    soma+=matriz[n][i]

media = soma / 12

if letra == 'S':
    print(f'{soma:.1f}')

elif letra == 'M':
    print(f'{media:.1f}')


