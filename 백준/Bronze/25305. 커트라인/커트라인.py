N, k = map(int, input().split())
s_list = list(map(int, input().split()))

temp = 0
for i in range(N):
    for j in range((N-1)-i):
        if s_list[j] < s_list[j+1]:
            temp = s_list[j+1]
            s_list[j+1] = s_list[j]
            s_list[j] = temp
print(f"{s_list[k-1]}")