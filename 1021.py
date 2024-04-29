entrada = float(input())
nota100 = int(entrada // 100)
resto = entrada % 100
nota50 = int(resto // 50)
resto -= nota50 * 50
nota20 = int(resto // 20)
resto -= nota20 * 20
nota10 = int(resto // 10)
resto -= nota10 * 10
nota5 = int(resto // 5)
resto -= nota5 * 5
nota2 = int(resto // 2)
resto -= (nota2 * 2)
resto = round(resto, 4)
moeda1 = int(resto // 1)
resto -= moeda1 * 1
resto = round(resto, 4)
moeda50 = int(resto // 0.5)
resto -= moeda50 * 0.5
resto = round(resto, 4)
moeda25 = int(resto // 0.25)
resto -= moeda25 * 0.25
resto = round(resto, 4)
moeda10 = int(resto // 0.10)
resto -= moeda10 * 0.10
resto = round(resto, 4)
moeda5 = int(resto // 0.05)
resto = resto - (moeda5) * 0.05
resto = round(resto, 4)
moeda01 = int(resto / 0.01)


print(f'NOTAS:\n{nota100} nota(s) de R$ 100.00\n{nota50} nota(s) de R$ 50.00\n{nota20} nota(s) de R$ 20.00\n{nota10} nota(s) de R$ 10.00\n{nota5} nota(s) de R$ 5.00\n{nota2} nota(s) de R$ 2.00')

print(f'MOEDAS:\n{moeda1} moeda(s) de R$ 1.00\n{moeda50} moeda(s) de R$ 0.50\n{moeda25} moeda(s) de R$ 0.25\n{moeda10} moeda(s) de R$ 0.10\n{moeda5} moeda(s) de R$ 0.05\n{moeda01} moeda(s) de R$ 0.01')
