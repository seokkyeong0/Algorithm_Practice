V = int(input())
G = input()

a_cnt = 0
b_cnt = 0
for ch in G:
    if ch == 'A':
        a_cnt += 1
    elif ch == 'B':
        b_cnt += 1

if a_cnt > b_cnt:
    print(f"A")
elif a_cnt < b_cnt:
    print(f"B")
else:
    print(f"Tie")