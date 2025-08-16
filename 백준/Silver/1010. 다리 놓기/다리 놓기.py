import math as m
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(f"{m.factorial(M) / (m.factorial(N) * m.factorial(M-N)):.0f}")