N = int(input())

line = 1
while N > line:   # 5 1
    N -= line     # 4 2
    line += 1     # 2 3

if line % 2 == 0:
    print(f"{N}/{line - N + 1}")
else:
    print(f"{line - N + 1}/{N}")