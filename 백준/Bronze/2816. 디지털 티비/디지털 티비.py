N = int(input())

c_list = []
for _ in range(N):
    c_list.append(input())

find_cnt = 0
for i in range(len(c_list)):
    if c_list[i] == "KBS1":
        break
    else:
        print(1, end="")
        find_cnt += 1

for i in range(find_cnt):
    c_list[find_cnt-i], c_list[find_cnt-1-i] = c_list[find_cnt-1-i], c_list[find_cnt-i]
    print(4, end="")

find_cnt = 0
for i in range(len(c_list)):
    if c_list[1] == "KBS2":
        break
        
    if c_list[i] == "KBS2":
        break
    else:
        print(1, end="")
        find_cnt += 1
        
for i in range(find_cnt - 1):
    c_list[find_cnt-i], c_list[find_cnt-1-i] = c_list[find_cnt-1-i], c_list[find_cnt-i]
    print(4, end="")