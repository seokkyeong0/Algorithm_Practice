N = int(input())
c_list = [tuple(map(int, input().split())) for _ in range(N)]

c_list.sort(key=lambda x: (x[0], x[1]))

for x, y in c_list:
    print(x, y)