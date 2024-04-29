n = int(input())
for i in range(n):
    soma = 0
    x,y = map(int, input().split())
    
    if x % 2 != 0:
        for j in range(y):
            soma += x
            x +=2
    else:
        x = x+1
        for j in range(y):
            soma += x
            x +=2
    

    print(soma)
