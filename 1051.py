entrada = float(input())
isento = 2000
if (0 <= entrada <= 2000 ):
    print('Isento')

elif (2000.01 <= entrada <= 3000):
    imposto = (entrada - isento) * (8 / 100)
    print(f'R$ {imposto:.2f}')

elif (3000.01 <= entrada <= 4500):
    impostobase = 1000 * (8 / 100)
    imposto = ((entrada - 3000) * (18 / 100)) + impostobase
    print(f'R$ {imposto:.2f}')

elif (entrada > 4500):
    impostobase = 1000 * (8 / 100)
    impostobase2 = 1500 * (18 / 100)
    imposto = ((entrada - 4500) * (28 / 100)) + impostobase + impostobase2
    print(f'R$ {imposto:.2f}')

