import sys
input = sys.stdin.readline

N = int(input())
memo = [0] * (N+3)

def tile_01(num):
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    if num < 3:
        return memo[num]
    else:
        for i in range(3, num + 1):
            memo[i] = (memo[i-1] + memo[i-2]) % 15746
        return memo[num]
print(f"{tile_01(N)}")