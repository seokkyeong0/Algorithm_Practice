import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

dq = deque()
for i in range(N-1, -1, -1):
    if A[i] == 0:
        dq.append(B[i])

out = []
for num in C:
    dq.append(num)
    out.append(str(dq.popleft()))

sys.stdout.write(" ".join(out))