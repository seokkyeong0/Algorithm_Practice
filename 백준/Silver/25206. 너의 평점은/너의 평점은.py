s_list = []
for i in range(20):
    s_list.append(list(input().split()))

m_cnt = 0
s_cnt = 0
for i in range(len(s_list)):
    if s_list[i][2] == "A+":
        s_cnt += float(s_list[i][1]) * 4.5
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "A0":
        s_cnt += float(s_list[i][1]) * 4.0
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "B+":
        s_cnt += float(s_list[i][1]) * 3.5
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "B0":
        s_cnt += float(s_list[i][1]) * 3.0
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "C+":
        s_cnt += float(s_list[i][1]) * 2.5
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "C0":
        s_cnt += float(s_list[i][1]) * 2.0
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "D+":
        s_cnt += float(s_list[i][1]) * 1.5
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "D0":
        s_cnt += float(s_list[i][1]) * 1.0
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "F":
        s_cnt += float(s_list[i][1]) * 0.0
        m_cnt += float(s_list[i][1])
    if s_list[i][2] == "P":
        continue
print(f"{s_cnt / m_cnt}")