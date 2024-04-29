op = input()
matriz = []
for i in range(3):
    matriz_linha = []
    for j in range(3):
        matriz_linha.append(float(input()))
    matriz.append(matriz_linha[i+1:])

soma = 0
elementos = 0
for linha in matriz:
    for elemento in linha:
        soma+= elemento
        elementos+= 1

media = soma / elementos

if op =='S':
    print(soma)
    
elif op =='M':
    print(media)



