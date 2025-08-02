A, B, C = map(int, input().split())

price = 0

if A == B == C:
    price = 10000 + (A*1000)
elif A == B:
    price = 1000 + (A*100)
elif B == C:
    price = 1000 + (B*100)
elif A == C:
    price = 1000 + (A*100)
else:
    if A > B and A > C:
        price = A*100
    if B > A and B > C:
        price = B*100
    if C > A and C > B:
        price = C*100
print(price)