n = int(input())
for i in range (n):
    i = list(map(float,input().split()))
    media = ((i[0] * 2) + (i[1] * 3) + (i[2] * 5)) / 10
    print(f'{media:.1f}')
    