x = int(input())
vetor = list(map(int, input().split()))
menor = vetor[0]
for i, num in enumerate(vetor):
    if num < menor:
        menor = num
        pos = i
print(f'Menor valor: {menor}\nPosicao: {pos}')

