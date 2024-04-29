n = int(input())
soma_qtd_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0


for i in  range(n):
    entrada = input().split()
    qtd_cobaias = int(entrada[0])
    tipo = entrada[1]
    soma_qtd_cobaias += qtd_cobaias

    if (tipo == 'C'):
        total_coelhos += qtd_cobaias
    
    elif (tipo == 'R'):
        total_ratos += qtd_cobaias

    else:
        total_sapos += qtd_cobaias

percentual_coelhos = (total_coelhos / soma_qtd_cobaias) * 100
percentual_ratos = (total_ratos / soma_qtd_cobaias) * 100
percentual_sapos = (total_sapos / soma_qtd_cobaias) * 100

print (f'Total: {soma_qtd_cobaias} cobaias\nTotal de coelhos: {total_coelhos}\nTotal de ratos: {total_ratos}\nTotal de sapos: {total_sapos}\nPercentual de coelhos: {percentual_coelhos:.2f} %\nPercentual de ratos: {percentual_ratos:.2f} %\nPercentual de sapos: {percentual_sapos:.2f} %')

     


