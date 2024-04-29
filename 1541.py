while True:
    entrada = input().split()
    if entrada[0] == '0':
        break
    a, b, c = map(int, entrada)
    area = a * b
    area_max = (area * 100) / c
    lado = int(area_max ** 0.5)
    print(lado)