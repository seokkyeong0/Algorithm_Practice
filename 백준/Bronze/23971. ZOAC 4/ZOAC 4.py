def upup(num):
    if num % 1 > 0:
        return num - (num % 1) + 1
    else:
        return num
        
H, W, N, M = map(int, input().split())
print(f"{upup(H/(N+1)) * upup(W/(M+1)):.0f}")