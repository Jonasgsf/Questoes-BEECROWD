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
    
    