entradai = input().split()
diai = int(entradai[1])
h,m,s = map(int, input().split(':'))
entradaf = input().split()
diaf = int(entradaf[1])
hf,mf,sf = map(int, input().split(':'))


inicio_segundos = (diai * 24 * 3600) + (h * 3600) + (m * 60) + s
termino_segundos = (diaf * 24 * 3600) + (hf * 3600) + (mf * 60) + sf
diferenca_segundos = termino_segundos - inicio_segundos


qtd_dia = diferenca_segundos // (24 * 3600)
diferenca_segundos %= (24 * 3600)
hora = diferenca_segundos // 3600
diferenca_segundos %= 3600
minuto = diferenca_segundos // 60
diferenca_segundos %= 60
segundo = diferenca_segundos

print(f'{qtd_dia} dia(s)\n{hora} hora(s)\n{minuto} minuto(s)\n{segundo} segundo(s)')