N = int(input())
M = list(map(int, input().split()))
V = int(input())

count = 0
for i in M:
    if i == V:
        count += 1
print(f"{count}")