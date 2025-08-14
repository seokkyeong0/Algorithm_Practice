a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

# f(n) = a1*n + a0
# g(n) = n
# f(n) <= c * g(n)

is_valid = False
for i in range(n,101):
    if a1*i + a0 <= c * i:
        is_valid = True
    else:
        is_valid = False
        break

if is_valid:
    print(f"{1}")
else:
    print(f"{0}")