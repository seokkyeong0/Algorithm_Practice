x_list = []
y_list = []
for i in range(3):
    A, B = map(int, input().split())
    x_list.append(A)
    y_list.append(B)

x_list.sort()
y_list.sort()

x_index = 0
for x in x_list:
    if x == x_list[0]:
        x_index += 1

y_index = 0
for y in y_list:
    if y == y_list[0]:
        y_index += 1

if x_index > 1:
    print(f"{x_list[2]}", end=" ")
else:
    print(f"{x_list[0]}", end=" ")

if y_index > 1:
    print(f"{y_list[2]}", end="")
else:
    print(f"{y_list[0]}", end="")