# Baekjoon 2869 (B1)
A, B, V = map(int, input().split())
import math
day = math.ceil(((V-A)/(A-B))) + 1
print(f"{day}")