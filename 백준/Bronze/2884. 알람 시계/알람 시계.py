H, M = map(int, input().split())

temp_H = H
temp_M = M - 45

if temp_M < 0:
    temp_H -= 1
    temp_M = 60 - (45 - M)
if temp_H < 0:
    temp_H = 23
print(f"{temp_H} {temp_M}")