while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f'{abs(i - j) + 1:>3d}', end="")
            if j != n:
                print(" ", end="")
        print()  
    print()