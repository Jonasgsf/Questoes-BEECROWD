hi,hf = list(map(int, input().split()))
if hf <= hi:
    tempo = (24 - hi) + hf
    print(f'O JOGO DUROU {tempo} HORA(S)')
else:
    tempo = hf - hi
    print(f'O JOGO DUROU {tempo} HORA(S)')
