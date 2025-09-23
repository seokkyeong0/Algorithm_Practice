N = int(input())

for i in range(N):
    for a in range(i+1):
        print(f"*", end="")
    for b in range((2*(N-1))-(2*i)):
        print(f" ", end="")
    for c in range(i+1):
        print(f"*", end="")
    print()
for i in range(N-1):
    for a in range((N-1)-i):
        print(f"*", end="")
    for b in range(2*(i+1)):
        print(f" ", end="")
    for c in range((N-1)-i):
        print(f"*", end="")
    print()