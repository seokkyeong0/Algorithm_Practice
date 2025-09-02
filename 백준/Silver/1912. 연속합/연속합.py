N = int(input())
n_list = list(map(int, input().split()))

max_val = n_list[0]
current_sum = n_list[0]

for i in range(1, N):
    current_sum = max(n_list[i], current_sum + n_list[i])
    max_val = max(max_val, current_sum)

print(max_val)