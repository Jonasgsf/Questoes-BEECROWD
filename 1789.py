while True:
    try:
        t = input()
        if not t:
            break

        t = int(t)  
        lesmas = list(map(int, input().split()))
        maior = lesmas[0]
        for i in range(t):
            if lesmas[i] > maior:
                maior = lesmas[i]
        if maior < 10:
            print(1)
        elif 10 <= maior < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break
