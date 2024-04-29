n = int(input())
for i in range(n):
    soma = 0
    x,y = map(int,input().split())

    if x > y:
        x,y = y,x

    for impar in range(x,y):
        if (impar % 2 !=0) and (impar !=x and impar != y):
            soma += impar

    print(soma)
    
