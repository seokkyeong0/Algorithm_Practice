# Baekjoon 14626 (B1)
ISBN = input()

index = 0
check_sum = 0
for i in range(len(ISBN)-1):
    if ord(ISBN[i]) < 48:
        temp = index
        continue
    else:
        if i % 2 == 0:
            check_sum += ord(ISBN[i]) - 48
        else:
            check_sum += 3*(ord(ISBN[i]) - 48)
    index += 1

for i in range(10):
    if temp % 2 == 0 and ord(ISBN[-1]) - 48 == (10 - (check_sum + i)) % 10:
        print(f"{i}")
        break
    if (temp+1) % 2 == 0 and ord(ISBN[-1]) - 48 == (10 - (check_sum + 3*i)) % 10:
        print(f"{i}")
        break