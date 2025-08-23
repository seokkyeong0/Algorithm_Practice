T = int(input())

for _ in range(T):
    c_list = list(map(str, input().split()))
    cal = 0
    for i in c_list:
        if 48 <= ord(i[0]) <= 57:
           cal += float(i)
        elif i == "@":
            cal *= 3
        elif i == "%":
            cal += 5
        elif i == "#":
            cal -= 7
    print(f"{cal:.2f}")