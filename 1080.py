maior = 1
posicao = 1
for i in range(1,101):
    num = int(input())
    if num > maior:
        maior = num
        posicao = i
print(maior,posicao, sep ='\n')