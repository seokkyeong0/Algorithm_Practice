N = int(input())

def fibo(N):
    if N == 0:
        return 0
    elif N <= 2:
        return 1
    return fibo(N-1)+fibo(N-2)
print(f"{fibo(N)}")