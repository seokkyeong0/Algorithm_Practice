N, K = map(int, input().split())

import math
def bico(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(f"{bico(N, K):.0f}")