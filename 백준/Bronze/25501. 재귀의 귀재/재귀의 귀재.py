def recursion(char, l, r):
    global cnt
    cnt += 1
    if l >= r: 
        return 1
    elif char[l] != char[r]: 
        return 0
    else:
        return recursion(char, l+1, r-1)

def isPalindrome(char):
    return recursion(char, 0, len(char)-1)

N = int(input())
for _ in range(N):
    S = input()
    cnt = 0
    print(f"{isPalindrome(S)} {cnt}")