import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    next_prime = False
    P = int(input())
    
    while not(next_prime):
        next_prime = True
        for i in range(2, int(P**0.5) + 1):
            if P % i == 0:
                next_prime = False
                P += 1
                break

    if P < 2:
        print(f"{2}")
    else:
        print(f"{P}")