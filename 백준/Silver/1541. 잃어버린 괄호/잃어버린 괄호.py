E = input()

o_cnt = 0
for ch in E:
    if ch == "-" or ch == "+":
        o_cnt += 1

t_list = [[] for _ in range(o_cnt + 1)]
o_list = []

idx = 0
for ch in E:
    if ch != "+" and ch != "-":
        t_list[idx].append(int(ch))
    else:
        o_list.append(ch)
        idx += 1

n_list = []
for i in range(len(t_list)):
    cnt = 0
    for j in range(len(t_list[i])):
        cnt += int(t_list[i][j]) * (10 ** (len(t_list[i])-1-j))
    n_list.append(int(cnt))

is_sub = False
total = n_list[0]
for i in range(1, len(n_list)):
    if is_sub:
        total -= n_list[i]
            
    if o_list[i-1] == "+" and not(is_sub):
        total += n_list[i]
    elif o_list[i-1] == "-" and not(is_sub):
        total -= n_list[i]
        is_sub = True
print(total)