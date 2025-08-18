import math
A, B = map(int, input().split())
print(f"{A*B//math.gcd(A,B)}")