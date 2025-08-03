N, M = map(int, input().split())
basket = list(0 for i in range(N))

for i in range(M):
    A, B, C = map(int, input().split())
    for i in range(A-1, B):
        basket[i] = C
for i in range(N):
    print(f"{basket[i]}", end = " ")