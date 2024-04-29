salario = float(input())

if 0 <= salario <= 400:
    reajuste = salario * 0.15
    nsalario = salario + reajuste
    print(f'Novo salario: {nsalario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 15 %')
    
elif 400.01 <= salario <= 800:
    reajuste = salario * 0.12
    nsalario = salario + reajuste
    print(f'Novo salario: {nsalario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %')

elif 800.01 <= salario <= 1200:
    reajuste = salario * 0.10
    nsalario = salario + reajuste
    print(f'Novo salario: {nsalario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %')

elif 1200.01 <= salario <= 2000:
    reajuste = salario * 0.07
    nsalario = salario + reajuste
    print(f'Novo salario: {nsalario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 7 %')

elif 2000 < salario:
    reajuste = salario * 0.04
    nsalario = salario + reajuste
    print(f'Novo salario: {nsalario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 4 %')
