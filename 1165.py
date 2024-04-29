n = int(input())
for i in range(n):
    x = int(input())
    primo = 0
    for numero in range(2,x):
        if x % numero == 0:
            primo = 1
            
    if primo == 1:
        print(f'{x} nao eh primo')
            
    else: 
        print(f'{x} eh primo')
 