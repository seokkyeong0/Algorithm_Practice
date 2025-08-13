len_list = list(map(int, input().split()))
len_list.sort()

if len_list[2] < len_list[0] + len_list[1]:
    print(f"{len_list[0] + len_list[1] + len_list[2]}")
else:
    print(f"{2*(len_list[0] + len_list[1])-1}")