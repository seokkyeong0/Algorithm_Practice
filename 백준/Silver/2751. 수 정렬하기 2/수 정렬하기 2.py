import sys
N = int(sys.stdin.readline())
num_list = [0] * N

for i in range(N):
    num_list[i] = int(sys.stdin.readline())

num_list = sorted(set(num_list))
for num in num_list:
    print(f"{num}")