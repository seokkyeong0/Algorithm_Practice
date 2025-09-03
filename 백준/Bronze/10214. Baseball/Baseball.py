T = int(input())

for _ in range(T):
    y_cnt = 0
    k_cnt = 0
    
    for _ in range(9):
        Y, K = map(int, input().split())
        y_cnt += Y
        k_cnt += K
        
    if y_cnt > k_cnt:
        print(f"Yonsei")
    elif y_cnt < k_cnt:
        print(f"Korea")
    else:
        print(f"Draw")