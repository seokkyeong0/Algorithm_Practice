N = int(input())
n_list = list(map(int, input().split()))

n = [0] * 20000001
for i in n_list:
    n[10000000+i] += 1
    
M = int(input())
m_list = list(map(int, input().split()))

print(" ".join(str(n[10000000+i]) for i in m_list))