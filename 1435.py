while True:
    n = int(input())
    if n == 0:
        break
    
    matriz = [[0] * n for _ in range(n)]  

    for i in range(n):
        for j in range(n):
            matriz[i][j] = min(i, j, n - i - 1, n - j - 1) + 1

    for linha in matriz:
        print(' '.join(f'{num:>3d}' for num in linha))
    print()
