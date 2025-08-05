while True:
    S = int(input())
    P = str(S)
    is_palindrome = None
    cnt = 0
    if S == 0:
        break
    for i in range(int(len(P)/2)):
        if P[i] == P[-1-i]:
            cnt += 1
        else:
            continue
    if cnt == int(len(P)/2):
        is_palindrome = True
    else:
        is_palindrome = False
        
    if is_palindrome:
        print(f"yes")
    else:
        print(f"no")