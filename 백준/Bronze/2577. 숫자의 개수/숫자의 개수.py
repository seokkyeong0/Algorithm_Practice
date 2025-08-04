A = int(input())
B = int(input())
C = int(input())

digit = 0
for i in range(0, 10):
    for ch in str(A*B*C):
        if ch == str(i):
            digit += 1
    print(digit)
    digit = 0