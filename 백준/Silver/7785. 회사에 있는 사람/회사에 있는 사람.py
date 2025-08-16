N = int(input())

p_set = set()
for i in range(N):
    P, E = input().split()
    if E == "leave":
        p_set.discard(P)
    else:
        p_set.add(P)
        
for name in sorted(p_set, reverse=True):
    print(name)