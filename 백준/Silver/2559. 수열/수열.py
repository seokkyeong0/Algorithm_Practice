import sys
input = sys.stdin.readline

N, K = map(int, input().split())
t_list = list(map(int, input().split()))

window = sum(t_list[:K])
total = window
for i in range(K, N):
    window += t_list[i] - t_list[i-K]
    total = max(total, window)
print(f"{total}")