T = int(input())
s_cnt = 1
score = 0
for i in range(T):
    ox_data = input()
    for i in ox_data:
        if i == "O":
            score += s_cnt
            s_cnt += 1
        if i == "X":
            s_cnt = 1
    print(score)
    score = 0
    s_cnt = 1