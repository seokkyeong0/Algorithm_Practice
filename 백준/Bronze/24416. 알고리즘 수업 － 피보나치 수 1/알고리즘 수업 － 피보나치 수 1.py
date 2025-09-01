N = int(input())

cnt = 0
def fibonacci(N):
    global cnt
    memo = [0] * (N+1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    if N < 3:
        return memo[N]
    else:
        for i in range(3, N+1):
            cnt += 1
            memo[i] = memo[i-1] + memo[i-2]
        return memo[i]

result = fibonacci(N)
print(f"{result} {cnt}")