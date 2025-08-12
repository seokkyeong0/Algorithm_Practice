A = int(input())
B = int(input())
C = int(input())

if A == B == C == 60:
    print(f"Equilateral")
elif A + B + C == 180:
    if A == B:
        print(f"Isosceles")
    elif B == C:
        print(f"Isosceles")
    elif A == C:
        print(f"Isosceles")
    else:
        print(f"Scalene")
else:
    print(f"Error")