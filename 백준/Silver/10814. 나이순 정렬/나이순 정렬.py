N = int(input())

c_list = []
for i in range(N):
    c_list.append(input().split())

c_list.sort(key=lambda x: int(x[0]))

for i in range(len(c_list)):
    print(f"{c_list[i][0]} {c_list[i][1]}")