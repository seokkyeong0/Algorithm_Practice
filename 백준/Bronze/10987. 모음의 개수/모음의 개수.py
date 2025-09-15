S = input()

cnt = 0
for ch in S:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        cnt += 1
print(f"{cnt}")