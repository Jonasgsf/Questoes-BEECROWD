
while True:
    notas_validas = 0
    media = 0
    soma = 0
    while True:
        if notas_validas == 2:
            break 
        nota = float(input())

        if (nota < 0 ) or (nota > 10):
            print('nota invalida')

        else:
            notas_validas += 1
            media += 1
            soma += nota

    print(f'media = {soma / media:.2f}')
    x = int(input('novo calculo (1-sim 2-nao)\n'))

    while (x < 1) or (x > 2):
        x = int (input('novo calculo (1-sim 2-nao)\n'))
        if (x == 1) or (x == 2):
            break
    if x == 2:
        break

    

    