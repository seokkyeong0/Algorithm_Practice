x, y, w, h = map(int, input().split())

dis_x = abs(x-w)
dis_y = abs(y-h)

if dis_x >= x and dis_y >= y:
    if x >= y:
        print(f"{y}")
    else:
        print(f"{x}")
elif dis_x <= x and dis_y <= y:
    if dis_x >= dis_y:
        print(f"{dis_y}")
    else:
        print(f"{dis_x}")
elif dis_x >= x and dis_y <= y:
    if x >= dis_y:
        print(f"{dis_y}")
    else:
        print(f"{x}")
else:
    if dis_x >= y:
        print(f"{y}")
    else:
        print(f"{dis_x}")