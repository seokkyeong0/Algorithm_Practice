N, M = map(int, input().split())
basket = list(i+1 for i in range(N))
temp = 0
for i in range(M):
    A, B = map(int, input().split())
    for i in range(((B-A)//2)+1):
        temp = basket[(A-1)+i]
        basket[(A-1)+i] = basket[(B-1)-i]
        basket[(B-1)-i] = temp
for i in range(N):
    print(f"{basket[i]}", end = " ")