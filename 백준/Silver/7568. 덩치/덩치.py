N = int(input())
d_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if d_list[j][0] > d_list[i][0] and d_list[j][1] > d_list[i][1]:
            rank += 1
    print(rank, end=" ")