ch = input()

i = 0
a_cnt = 0

while i < len(ch):
    if i + 2 < len(ch) and ch[i] == 'd' and ch[i+1] == 'z' and ch[i+2] == '=':
        a_cnt += 1
        i += 3
    elif i + 1 < len(ch):
        if ch[i] == 'c' and ch[i+1] == '=':
            a_cnt += 1
            i += 2
        elif ch[i] == 'c' and ch[i+1] == '-':
            a_cnt += 1
            i += 2
        elif ch[i] == 'd' and ch[i+1] == '-':
            a_cnt += 1
            i += 2
        elif ch[i] == 'l' and ch[i+1] == 'j':
            a_cnt += 1
            i += 2
        elif ch[i] == 'n' and ch[i+1] == 'j':
            a_cnt += 1
            i += 2
        elif ch[i] == 's' and ch[i+1] == '=':
            a_cnt += 1
            i += 2
        elif ch[i] == 'z' and ch[i+1] == '=':
            a_cnt += 1
            i += 2
        else:
            a_cnt += 1
            i += 1
    else:
        a_cnt += 1
        i += 1
print(a_cnt)