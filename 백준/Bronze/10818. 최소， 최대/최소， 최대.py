N = int(input())
M = list(map(int, input().split()))
max = M[0]
min = M[0]
for i in M:
    if max < i:
        max = i
    if min > i:
        min = i
print(f"{min} {max}")