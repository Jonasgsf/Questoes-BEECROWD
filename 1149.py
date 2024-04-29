entrada = input().split()

A = int(entrada[0])
N = int(entrada[-1])

while N <= 0:
    entrada = input().split()
    N = int(entrada[-1])

soma = 0
for i in range(N):
    soma += A + i

print(soma)
