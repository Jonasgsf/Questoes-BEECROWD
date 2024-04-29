op = input()
soma = 0
qtd = 0
for i in range(12):
    for j in range(12):
        matriz_linha = float(input())
        if (11 - i < j) and (j > i):
            soma += matriz_linha
            qtd += 1

media = soma / qtd
if op =='S':
    print(f'{soma:.1f}')   

elif op =='M':
    print(f'{media:.1f}')

