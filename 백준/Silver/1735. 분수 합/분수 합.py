import math
A_s, A_p = map(int, input().split())
B_s, B_p = map(int, input().split())

C_s = (A_s * B_p) + (A_p * B_s)
C_p = A_p * B_p

x = math.gcd(C_s, C_p)
C_s = C_s // x
C_p = C_p // x

print(f"{C_s} {C_p}")