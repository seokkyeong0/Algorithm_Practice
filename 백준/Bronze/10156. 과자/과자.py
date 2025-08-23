K, N, M = map(int, input().split())

if K*N < M:
    print(f"{0}")
else:
    print(f"{K*N-M}")