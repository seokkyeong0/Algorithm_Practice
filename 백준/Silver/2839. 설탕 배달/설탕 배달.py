N = int(input())

cnt = 0
is_valid = True
while N > 0:
    if N % 5 == 0:
        N -= 5
        cnt += 1
    elif N % 3 == 0:
        N -= 3
        cnt += 1
    elif N // 5 > 0 and N % 3 < 3:
        N -= 5
        cnt += 1
    else:
        is_valid = False
        break

if is_valid:
    print(f"{cnt}")
else:
    print(f"{-1}")