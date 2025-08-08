N, B = map(str, input().split())
total = 0
for i in range(len(N)):
    if ord(N[-(i+1)]) >= 65:
        total += (ord(N[-(i+1)]) - 55) * (int(B)**i)
    if ord(N[-(i+1)]) < 65:
        total += (ord(N[-(i+1)]) - 48) * (int(B)**i)
print(total)