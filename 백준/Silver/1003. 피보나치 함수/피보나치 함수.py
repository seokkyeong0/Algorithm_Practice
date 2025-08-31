import sys
input = sys.stdin.readline

def fibonacci(N):
    global z_cnt, o_cnt
    z_cnt = [0] * ((N-2 if N > 2 else 0) + 3)
    o_cnt = [0] * ((N-2 if N > 2 else 0) + 3)
    
    z_cnt[0] = 0
    z_cnt[1] = 0
    z_cnt[2] = 1
    
    o_cnt[0] = 0
    o_cnt[1] = 1
    o_cnt[2] = 1

    if N == 0:
        z_cnt[0] = 1
        o_cnt[0] = 0
    elif N == 1:
        z_cnt[1] = 0
        o_cnt[1] = 1
    
    for i in range(3, N + 1):
        z_cnt[i] = z_cnt[i-2] + z_cnt[i-1]
        o_cnt[i] = o_cnt[i-2] + o_cnt[i-1]    

# 0 0 (0)
# 0 1 (1)
# 1 1 (2)
# 1 2 (3)
# 2 3 (4)
# 3 5 (5)
# 5 8 (6)

T = int(input())
for _ in range(T):
    N = int(input())

    fibonacci(N)
    if N == 0:
        print(f"{z_cnt[0]} {o_cnt[0]}")
    elif N == 1:
        print(f"{z_cnt[1]} {o_cnt[1]}")
    elif N == 2:
        print(f"{z_cnt[2]} {o_cnt[2]}")
    else:
        print(f"{z_cnt[-1]} {o_cnt[-1]}")