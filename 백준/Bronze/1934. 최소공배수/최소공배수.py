T = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(T):
    A, B = map(int, input().split())
    result = (A*B) // gcd(A, B)
    print(result)