a,b,c = list(map(float,input().split()))

delta = (b ** 2) - (4 * a * c)

if (delta >= 0) and ((2 * a) != 0):
  raiz1= (- b + (delta ** 0.5)) / (2 * a)
  raiz2 = (- b - (delta ** 0.5)) / (2 * a)
  print(f'R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}')

else:
 print('Impossivel calcular')
