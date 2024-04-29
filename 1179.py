impares = []
pares = []
for i in range(15):
    x = int(input())

    if x % 2 ==0:
        pares.append(x)

        if len(pares)==5:
            for j, num in enumerate(pares):
                print(f'par[{j}] = {num}')
                pares = []
    else:
        impares.append(x)

        if len(impares) == 5:
                for j, num in enumerate(impares):
                    print(f'impar[{j}] = {num}') 
                    impares = []

for i in range(len(impares)):
    print(f'impar[{i}] = {impares[i]}')
for i in range(len(pares)):
    print(f'par[{i}] = {pares[i]}')
