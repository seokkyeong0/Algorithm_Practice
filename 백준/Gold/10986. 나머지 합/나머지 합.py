N, M = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * M
pf = 0
for i in range(N):
    pf += a[i]
    r[pf % M] += 1

ans = r[0]
for i in range(M):
    ans += r[i] * (r[i]-1) // 2
print(ans)