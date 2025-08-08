N = int(input())

dot_cnt = 25
i_cnt = 3
if N == 1:
    dot_cnt = 9
if N == 2:
    dot_cnt = 25
if N > 2:
    for i in range(N-2):
        if i > 0:
            i_cnt += 2**(i+1)
        dot_cnt += 5 + 4 * (2 * i_cnt) + 3 * ((i_cnt)**2)
print(f"{dot_cnt}")