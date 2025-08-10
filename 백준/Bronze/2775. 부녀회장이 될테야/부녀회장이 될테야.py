T = int(input())

def vill_num(k, n):
    memo = [0] * ((k*n)+n)
    for i in range(1,n+1):
        memo[i-1] = i
    for a in range(k):
        for b in range(n):
            for c in range(b+1):
                memo[(a+1)*n+b] += memo[(a*n)+c]
    return memo[-1]
            
for i in range(T):
    k = int(input())
    n = int(input())
    print(f"{vill_num(k,n)}")