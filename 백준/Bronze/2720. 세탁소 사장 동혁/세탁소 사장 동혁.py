T = int(input())

for i in range(T):
    q_cnt = 0
    d_cnt = 0
    n_cnt = 0
    p_cnt = 0
    
    C = int(input())
    q_cnt = C // 25
    d_cnt = C % 25 // 10 
    n_cnt = C % 25 % 10 // 5
    p_cnt = C % 25 % 10 % 5 // 1
    print(f"{q_cnt} {d_cnt} {n_cnt} {p_cnt}")