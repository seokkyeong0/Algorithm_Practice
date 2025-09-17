def adapter(W, A, V):
    if W >= A * V:
        return 1
    else:
        return 0

A = int(input())
W, V = map(int, input().split())
result = adapter(W, A, V)
print(f"{result}")