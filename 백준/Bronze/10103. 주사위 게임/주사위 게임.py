n = int(input())

cy = 100
sd = 100
for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        sd -= a
    elif a < b:
        cy -= b
    else:
        continue

print(f"{cy}")
print(f"{sd}")