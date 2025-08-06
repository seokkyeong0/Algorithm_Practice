N, M = map(int, input().split())

temp_A = [0] * N
temp_B = [0] * N

for i in range(N):
    num_list_A = list(map(int, input().split()))
    temp_A[i] = num_list_A

for i in range(N):
    num_list_B = list(map(int, input().split()))
    temp_B[i] = num_list_B

temp_sum = 0
for i in range(N):
    for j in range(M):
        temp_sum = temp_A[i][j] + temp_B[i][j]
        print(f"{temp_sum}", end=" ")
        temp_sum = 0
    print()