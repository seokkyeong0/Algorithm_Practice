N = int(input())

cnt = 0
c_set = set()
for i in range(N):
    s = input()
    if s == "ENTER":
        c_set.clear()
    else:
        if s not in c_set:
            cnt += 1
            c_set.add(s)
print(f"{cnt}")