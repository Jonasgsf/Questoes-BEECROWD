hi,mi,hf,mf = list(map(int, input().split()))
if (hf <= hi) and (mf == mi):
    tempoh = (24 - hi) + hf
    tempom = 0
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')

elif (hf == hi) and (mf > mi):
    tempoh = 0
    tempom = mf - mi
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')

elif (hf <= hi) and (mf < mi):
    tempoh = (23 - hi) + hf
    tempom = 60 - (mi - mf)
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')

elif (hf > hi) and (mf == mi):
    tempoh = hf - hi
    tempom = 0
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')

elif (hf > hi) and (mf > mi):
    tempoh = hf - hi
    tempom = mf - mi
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')

else:
    tempoh = (hf - hi) - 1
    tempom = 60 - (mi - mf)
    print(f'O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)')
