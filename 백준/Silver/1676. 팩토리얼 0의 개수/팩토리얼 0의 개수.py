import math
N = int(input())
cnt = 0
for ch in str(math.factorial(N))[::-1]:
    if ch != "0":
        break
    else:
        cnt += 1
print(f"{cnt}")