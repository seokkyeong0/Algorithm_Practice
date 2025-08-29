from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    prior = list(map(int, input().split()))
    
    q = deque()
    for i in range(N):
        q.append(i)
    
    result = []
    while q:
        max_priority = max(prior[i] for i in q)
        current = q.popleft()
        if prior[current] != max_priority:
            q.append(current)
        else:
            result.append(current)
            if current == M:
                print(len(result))
                break