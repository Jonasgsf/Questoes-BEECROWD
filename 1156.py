s = 1
d = 2
for i in range(3,40,2):
    s+= i/d
    d *= 2
    
print(f'{s:.2f}')