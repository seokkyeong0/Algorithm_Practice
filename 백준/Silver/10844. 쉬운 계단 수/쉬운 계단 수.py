N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for d in range(10):
        if d > 0:
            dp[i][d] += dp[i-1][d-1]
        if d < 9:
            dp[i][d] += dp[i-1][d+1]
        dp[i][d] %= 1000000000
print(sum(dp[N]) % 1000000000)