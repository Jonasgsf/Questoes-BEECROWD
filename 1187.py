op = input()
matriz = []
for i in range(6):
    matriz_linha = []
    for j in range(12):
        matriz_linha.append(float(input()))
    matriz_linha = matriz_linha[::-1][i +1 :]
    matriz_linha = matriz_linha[::-1][i +1 :] 
    matriz.append(matriz_linha)


soma = 0
elementos = 0
for linha in matriz:
    for elemento in linha:
        soma+= elemento
        elementos+= 1

media = soma / elementos

if op =='S':
    print(f'{soma:.1f}')
    
elif op =='M':
    print(f'{media:.1f}')

