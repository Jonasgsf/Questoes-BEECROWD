
fibo = [0,1]
n = int(input())
for i in range(n - 2):
    ultimo = fibo[-1]
    penultimo = (fibo[::-1])[1]
    fibo.append(penultimo + ultimo)

for i in range(len(fibo) -1):
    print(fibo[i], end = ' ')
print(fibo[-1])
    

