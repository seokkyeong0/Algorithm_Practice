import sys
input = sys.stdin.readline
N = int(input())

m_list = []
for _ in range(N):
    a, b = map(int, input().split())
    m_list.append([a, b])

m_list.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end = 0
for i in range(N):
    if end <= m_list[i][0]:
        end = m_list[i][1]
        cnt += 1
print(cnt)