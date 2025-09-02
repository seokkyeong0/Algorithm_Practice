import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))

prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + n_list[i]

output = []
for _ in range(M):
    A, B = map(int, input().split())
    output.append(str(prefix[B] - prefix[A-1]))

sys.stdout.write('\n'.join(output))