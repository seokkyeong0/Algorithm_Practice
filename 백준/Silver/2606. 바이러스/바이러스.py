v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, count):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            count = dfs(node, count+1)
    return count

visited = [False for _ in range(v+1)]
print(dfs(1, 0))