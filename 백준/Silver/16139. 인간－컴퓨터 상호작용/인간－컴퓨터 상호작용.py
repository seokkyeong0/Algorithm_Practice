import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input().rstrip())

pre = [[0] * 26]
for i, c in enumerate(S):
    pre.append(pre[len(pre) - 1][:])
    pre[i+1][ord(c)-97] += 1

for _ in range(q):
    q1, q2, q3 = input().rstrip().split()
    result = pre[int(q3) + 1][ord(q1) - 97] - pre[int(q2)][ord(q1) - 97]
    print(result)