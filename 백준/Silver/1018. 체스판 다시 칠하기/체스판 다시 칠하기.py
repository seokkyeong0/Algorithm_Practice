N, M = map(int, input().split())

m_list = []
for i in range(N):
    m_list.append(input())

chess = ""
chess2 = ""
c_list = []
c2_list = []
for i in range(1, N+1):
    if i % 2 != 0:
        chess += "W"
        chess2 += "B"
    else:
        chess += "B"
        chess2 += "W"
    for j in range(1, M):
        if i % 2 != 0:
            if j % 2 == 0:
                chess += "W"
                chess2 += "B"
            else:
                chess += "B"
                chess2 += "W"
        else:
            if j % 2 != 0:
                chess += "W"
                chess2 += "B"
            else:
                chess += "B"
                chess2 += "W"
    c_list.append(chess)
    c2_list.append(chess2)
    chess = ""
    chess2 = ""

cnt = 0
cnt2 = 0
cnt_list = []
for a in range((N+1)-8):
    for b in range((M+1)-8):
        for i in range(8):
            for j in range(8):
                if c_list[i+a][j+b] != m_list[i+a][j+b]:
                    cnt += 1
                if c2_list[i+a][j+b] != m_list[i+a][j+b]:
                    cnt2 += 1
        cnt_list.append(cnt)
        cnt_list.append(cnt2)
        cnt = 0
        cnt2 = 0
print(min(cnt_list))