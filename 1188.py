op = input()
matriz = []
for i in range(12):
    matriz_linha = []
    for j in range(12):
        matriz_linha.append(float(input()))
    matriz.append(matriz_linha)

matriz = matriz[::-1][:6]
nova_matriz = []

for i in range(6):
    matriz_linha = matriz[i][::-1][i + 1:]
    matriz_linha = matriz_linha[::-1][i + 1:]
    nova_matriz.append(matriz_linha) 

soma = 0
elementos = 0
for linha in nova_matriz:
    for elemento in linha:
        soma+= elemento
        elementos+= 1

media = soma / elementos

if op =='S':
    print(f'{soma:.1f}')
    
elif op =='M':
    print(f'{media:.1f}')


