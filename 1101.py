m, n = map(int, input().split())

while (m > 0) and (n > 0):
    if n < m:
        m, n = n, m

    soma = 0
    i = m
    conjuntoi = []
    while (m <= i <= n):
        soma += i
        conjuntoi.append(str(i)) 
        i += 1
    print(' '.join(conjuntoi), ' Sum=', soma, sep='')
    m, n = map(int, input().split())
