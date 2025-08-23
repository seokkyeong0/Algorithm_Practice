S = input()

cnt = 10
for i in range(1,len(S)):
    if S[i-1] == ")" and S[i] == "(":
        cnt += 10
        
    if S[i-1] == "(" and S[i] == ")":
        if i > 1 and S[i-2] == "(":
            cnt += 10
        elif i > 1 and S[i-2] == ")":
            cnt += 10
        elif i == 1:
            cnt += 10
            
    if S[i-1] == "(" and S[i] == "(":
        cnt += 5
        
    if S[i-1] == ")" and S[i] == ")":
        cnt += 5

print(f"{cnt}")