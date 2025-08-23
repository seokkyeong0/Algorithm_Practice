N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    if e-c > r:
        print(f"advertise")
    elif e-c == r:
        print(f"does not matter")
    else:
        print(f"do not advertise")