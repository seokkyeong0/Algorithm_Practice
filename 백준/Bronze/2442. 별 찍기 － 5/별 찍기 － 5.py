N = int(input())

for i in range(N):
    for j in range((N-1)-i):
        print(f" ", end="")
    for k in range((2*(i+1))-1):
        print(f"*", end="")
    print()