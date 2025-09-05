N = int(input())

r = [0] * (N+1)
g = [0] * (N+1)
b = [0] * (N+1)

for i in range(1, N+1):
    R, G, B = map(int, input().split())
    r[i], g[i], b[i] = R, G, B

memo = [[0]*3 for _ in range(N+1)]

memo[1][0] = r[1]
memo[1][1] = g[1]
memo[1][2] = b[1]

for i in range(2, N+1):
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + r[i]
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + g[i]
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + b[i]

print(min(memo[N][0], memo[N][1], memo[N][2]))