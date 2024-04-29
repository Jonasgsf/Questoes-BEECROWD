grenal = 0
gremio = 0
inter = 0
empate = 0
while True:
    i,g = map(int, input().split())
    if i > g:
        inter += 1
    elif g > i:
        gremio += 1
    
    else:
      empate += 1

    grenal += 1

    novo_grenal = int(input('Novo grenal (1-sim 2-nao)\n'))

    if novo_grenal == 2:
        break
   
print(f'{grenal} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}')

if inter > gremio:
   print('Inter venceu mais')

elif gremio > inter:
   print('Gremio venceu mais')

else: 
   print('Nao houve vencedor')

