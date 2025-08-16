# Baekjoon 18870 (S2)
N = int(input())
x = list(map(int, input().split()))

x_sorted = sorted(set(x))
rank = {num: idx for idx, num in enumerate(x_sorted)}
result = [rank[num] for num in x]
print(*result)