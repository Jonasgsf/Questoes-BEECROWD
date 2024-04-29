lista_x = []

for i in range(20):
    x = int(input())
    lista_x.append(x)

lista_x_reverse = lista_x[::-1]
for i in range(20):
    print(f'N[{i}] = {lista_x_reverse[i]}')