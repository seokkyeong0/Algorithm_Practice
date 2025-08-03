N = int(input())
for i in range(N):
    for _ in range((N-1)-i):
        print(f" ", end="")
    for _ in range(i+1):
        print(f"*", end="")
    print()