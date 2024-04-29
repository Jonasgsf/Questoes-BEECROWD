
media = 0
soma = 0
while True:
    idade = float(input())
    if idade < 0: break
    soma+= idade
    media += 1
print(f'{(soma / media):.2f}')

