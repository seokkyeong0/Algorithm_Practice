# Baekjoon 28702 (B1)
A = input()
B = input()
C = input()

i = 0
if ord(A[0]) < 65:
    i = int(A) + 3
if ord(B[0]) < 65:
    i = int(B) + 2
if ord(C[0]) < 65:
    i = int(C) + 1

if i % 3 == 0 and i % 5 == 0:
    print(f"FizzBuzz")
elif i % 3 == 0 and i % 5 != 0:
    print(f"Fizz")
elif i % 3 != 0 and i % 5 == 0:
    print(f"Buzz")
else:
    print(f"{i}")