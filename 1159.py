flag = 0
x = int(input())
while x != flag:
    soma = 0
    if x % 2 != 0:
        x = x+1

    for i in range(5):
            soma += x
            x+= 2
    print(soma)
    x = int(input())