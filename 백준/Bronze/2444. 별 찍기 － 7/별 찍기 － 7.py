N = int(input())
for i in range(N, 0, -1):
    for j in range(i-1):
        print(f" ", end="")
    for k in range((N+1)-i):
        print(f"*", end="")
    for m in range(N-i):
        print(f"*", end="")
    print()
for i in range(N-1):
    for j in range(1, i+2):
        print(f" ", end="")
    for k in range((N-1)-i):
        print(f"*", end="")
    for m in range((N-2)-i):
        print(f"*", end="")
    print()