N, M = map(int, input().split())

n_list = []
m_list = []
for n in range(N):
    n_list.append(input())
for m in range(M):
    m_list.append(input())

n_list = set(n_list)

cnt = 0
for s in m_list:
    if s in n_list:
        cnt += 1
print(cnt)