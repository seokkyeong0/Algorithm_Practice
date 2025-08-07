N = int(input())

S = [0] * N
for i in range(N):
    S[i] = input()

a_list = [chr(i+97) for i in range(26)]
cnt = 0
for i in range(0, N):
    s_list = [0] * 26
    t_list = [0] * 26
    if '' != S[i]:
        for _ in range(0, len(S[i])-1):
            if S[i][_] == S[i][_+1]:
                s_list[ord(S[i][_])-97] += 1
        for _ in range(0, len(S[i])):
            if S[i][_] in a_list:
                t_list[ord(S[i][_])-97] += 1
    
        for _ in range(26):
            if t_list[_] > 0:
                t_list[_] -= 1
    
        is_group = True
        for j in range(26):
            if s_list[j] != t_list[j]:
                is_group = False
                break
        if is_group:
            cnt += 1
        else:
            continue
    else:
        continue
print(f"{cnt}")