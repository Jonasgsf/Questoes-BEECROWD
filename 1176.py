n = int(input())
for i in range(n):
    fibo = [0,1]
    x = int(input())
    for i in range(2,x +1):
        ultimo = fibo[-1]
        penultimo = (fibo[::-1])[1]
        fibo.append(ultimo + penultimo)

    if x == 0:
        print(f'Fib({x}) = {fibo[0]}')
    else:
        print(f'Fib({x}) = {fibo[-1]}')