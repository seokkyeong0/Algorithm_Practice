S = input()

is_palindrome = None
cnt = 0

for i in range(int(len(S)/2)):
    if S[i] == S[-1-i]:
        cnt += 1
    else:
        continue
        
if cnt == int(len(S)/2):
    is_palindrome = True
else:
    is_palindrome = False
        
if is_palindrome:
    print(f"{1}")
else:
    print(f"{0}")