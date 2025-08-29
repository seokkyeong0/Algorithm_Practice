n = int(input())
stack = []
result = []
cur = 1
possible = True

for _ in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False

if possible:
    print("\n".join(result))
else:
    print("NO")