N = int(input())

n_list = [0] * (N+1)
for i in range(N):
    n_list[i+1] = list(map(int, input().split()))

memo = [[] for i in range(N+1)]
memo[1].append(n_list[1][0])

for i in range(2, N+1):
    for j in range(len(n_list[i])):
        if j == 0:
            memo[i].append(memo[i-1][0] + n_list[i][j])
        elif j == len(n_list[i]) - 1:
            memo[i].append(memo[i-1][-1] + n_list[i][j])
        else:
            memo[i].append(max(memo[i-1][j-1], memo[i-1][j]) + n_list[i][j])
print(f"{max(memo[-1])}")