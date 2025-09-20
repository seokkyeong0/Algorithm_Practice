N = int(input())

for i in range(N):
    for b in range(i):
        print(" ", end="")
    for a in range(N-i):
        print("*", end="")
    print()