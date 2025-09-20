import math

N = int(input())
def is_square(x):
    return int(math.isqrt(x))**2 == x

if is_square(N):
    print(1)
elif any(is_square(N - i*i) for i in range(1, int(math.isqrt(N)) + 1)):
    print(2)
else:
    found = False
    for i in range(1, int(math.isqrt(N)) + 1):
        for j in range(1, int(math.isqrt(N - i*i)) + 1):
            if is_square(N - i*i - j*j):
                found = True
                break
        if found:
            break
    if found:
        print(3)
    else:
        print(4)