N, M = map(int, input().split())

dmp = set()
bmp = set()
for _ in range(N):
    dmp.add(input())
for _ in range(M):
    bmp.add(input())

cnt = 0
dbmp = []
for p in dmp:
    if p in bmp:
        cnt += 1
        dbmp.append(p)

print(cnt)
dbmp.sort()
for p in dbmp:
    print(p)