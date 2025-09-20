T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        cloth, ctype = input().split()
        clothes[ctype] = clothes.get(ctype, 0) + 1
    
    result = 1
    for val in clothes.values():
        result *= (val + 1)
    print(result - 1)