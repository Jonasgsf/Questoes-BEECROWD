flag = 0
x = int(input())
while x != flag:
    for i in range(1, x+1):
       
        if i == x:
            print(i, end='')
            print()
        else:
            print(i, end= ' ')
    x = int(input())