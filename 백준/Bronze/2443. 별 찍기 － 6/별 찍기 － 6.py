N = int(input())

for i in range(N):
    for k in range(i):
        print(f" ", end="")
    for j in range(2*(N-i)-1):
        print(f"*", end="")
    print()