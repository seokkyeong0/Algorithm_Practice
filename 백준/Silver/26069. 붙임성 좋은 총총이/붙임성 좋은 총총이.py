N = int(input())

dance = {"ChongChong"}
for i in range(N):
    a, b = input().split()
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)
print(len(dance))