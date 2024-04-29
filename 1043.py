x,y,z = list(map(float, input().split()))
a,b,c =  sorted([x,y,z])
if (a + b) > c:
    print(f'Perimetro = {a + b + c:.1f}')
else:
    print(f'Area = {((x + y) * z) / 2:.1f}')