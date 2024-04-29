coluna = int(input())
operacao = input()
matriz = []

for i in range(12):
    coluna_matriz = []
    for j in range(12):
        
        coluna_matriz.append(float(input()))
    matriz.append(coluna_matriz)

soma = 0
for i in range(12):
    soma += matriz[i][coluna]

media = soma / 12

if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao =='M':
    print(f'{media:.1f}')