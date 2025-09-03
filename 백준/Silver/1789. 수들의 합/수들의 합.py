N = int(input())

i = 1
cnt = 0
total = 0
is_exceed = False
while total < N:
    total += i
    
    if total > N:
        is_exceed = True
        total -= i

    if is_exceed:
        i -= 1
    else:
        cnt += 1
        i += 1
    
print(f"{cnt}")