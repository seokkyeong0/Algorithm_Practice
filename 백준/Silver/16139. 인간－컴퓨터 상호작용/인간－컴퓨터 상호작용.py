import sys
input = sys.stdin.readline

S = input()
q = int(input())

pre = {ch: [0]*(len(S)+1) for ch in set(S)}

for i, c in enumerate(S):
    for ch in pre:
        pre[ch][i+1] = pre[ch][i] + (1 if c == ch else 0)

for _ in range(q):
    q1, q2, q3 = input().split()
    l = int(q2)
    r = int(q3)
    if q1 in pre:
        result = pre[q1][r+1] - pre[q1][l]
    else:
        result = 0
    print(result)