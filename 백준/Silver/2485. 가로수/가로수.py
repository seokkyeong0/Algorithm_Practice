T = int(input())

n_list = []
for _ in range(T):
    N = int(input())
    n_list.append(N)

diffs = []
for i in range(len(n_list)-1):
    diffs.append(n_list[i+1] - n_list[i])

import math
div = diffs[0]
for d in diffs[1:]:
    div = math.gcd(div, d)

cnt = 0
for i in range(len(n_list)-1):
    if n_list[i+1] - n_list[i] > div:
        cnt += ((n_list[i+1] - n_list[i]) // div) - 1

print(f"{cnt}")