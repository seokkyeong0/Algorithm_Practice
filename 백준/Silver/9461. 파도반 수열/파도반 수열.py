import sys
input = sys.stdin.readline

def padoban(num):
    memo = [0] * (num+6)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2
    if num < 6:
        return memo[num]
    else:
        for i in range(6, num + 1):
            memo[i] = memo[i-1] + memo[i-5]
        return memo[num]

T = int(input())
for _ in range(T):
    N = int(input())
    print(f"{padoban(N)}")