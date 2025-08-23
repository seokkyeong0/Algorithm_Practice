N = int(input())

price = 0
for _ in range(N):
    A, B, C = map(int, input().split())

    if A == B == C:
        if price < 10000+A*1000:
            price = 10000+A*1000
    elif A == B or B == C or A == C:
        if A == B:
            if price < 1000+A*100:
                price = 1000+A*100
        elif B == C:
            if price < 1000+B*100:
                price = 1000+B*100
        else:
            if price < 1000+C*100:
                price = 1000+C*100
    else:
        if A > B and A > C:
            if price < A*100:
                price = A*100
        elif B > A and B > C:
            if price < B*100:
                price = B*100
        else:
            if price < C*100:
                price = C*100
print(f"{price}")