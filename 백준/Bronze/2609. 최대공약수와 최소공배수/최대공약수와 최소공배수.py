A, B = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

g = gcd(A, B)
l = A * B // g

print(g)
print(l)