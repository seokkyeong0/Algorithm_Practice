N, K = map(int, input().split())
num_list = []
for i in range(1,N+1):
    if N % i == 0:
        num_list.append(i)

try:
    print(f"{num_list[K-1]}")
except:
    print(f"{0}")