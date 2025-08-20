N, M = map(int, input().split())

poke_list = {}
reverse_list = {}

for i in range(1, N+1):
    name = input().strip()
    poke_list[name] = i
    reverse_list[i] = name

for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(reverse_list[int(query)])
    else:
        print(poke_list[query])