lista_x =[]
for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    lista_x.append(x)

    print(f'X[{i}] = {lista_x[i]}')