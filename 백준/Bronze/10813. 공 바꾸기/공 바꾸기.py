N, M = map(int, input().split())
basket = list(i+1 for i in range(N))
temp = 0

for i in range(M):
    A, B = map(int, input().split())
    temp = basket[A-1]
    basket[A-1] = basket[B-1]
    basket[B-1] = temp
for i in range(N):
    print(f"{basket[i]}", end = " ")