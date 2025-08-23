A, B, C = map(int, input().split())
D = int(input())

A += D // 3600
B += (D % 3600) // 60
C += (D % 60)
    
if C > 59:
    B += C // 60
    C = C % 60

if B > 59:
    A += B // 60
    B = B % 60

if A > 23:
    A = A % 24

print(f"{A} {B} {C}")