N = int(input())

x_list = []
y_list = []

for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_len = max(x_list) - min(x_list)
y_len = max(y_list) - min(y_list)
print(f"{x_len * y_len}")