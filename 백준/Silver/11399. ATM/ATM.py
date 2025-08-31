N = int(input())
P = list(map(int, input().split()))
P.sort()

min_sum = 0
for i in range(len(P)):
    for j in range(1+i):
        min_sum += P[j]
print(f"{min_sum}")