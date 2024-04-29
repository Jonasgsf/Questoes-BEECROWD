
'''
for i in range(1,10,2):
        if i == 1:
           for j in range(7,4,-1):
            print(f'I={i} J={j}')

        if i == 3:
            for j in range(9,6,-1):
                print(f'I={i} J={j}')
        
        if i == 5:
            for j in range(11,8,-1):
                print(f'I={i} J={j}')
        
        if i == 7:
            for j in range(13,10,-1):
                print(f'I={i} J={j}')

        if i == 9:
            for j in range(15,12,-1):
                print(f'I={i} J={j}')
'''
acumulador= -2
for i in range(1,10,2):
    acumulador += 2
    for j in range(7,4,-1):
        print(f'I={i} J={j + acumulador}')

''' suetone:
for i in range(1, 10, 2):
    for j in range(i+6, i+3, -1):
        print(f'I={i} J={j}')
'''