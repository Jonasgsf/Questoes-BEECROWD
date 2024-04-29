n = int(input())
for i in range(n):
    i = int(input())

    if (i == 0 ):
        print('NULL')
    elif (i != 0) and (i % 2 == 0):
        if(i > 0):
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if (i > 0):
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')

