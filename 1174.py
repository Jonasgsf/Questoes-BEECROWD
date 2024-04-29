lista_x =[]
for i in range(100):
    x = float(input())
    lista_x.append(x)
    if x <= 10:
        print(f'A[{i}] = {lista_x[i]:.1f}')