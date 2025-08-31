import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_dict = {}
for _ in range(N):
    site, pw = input().split()
    site_dict[site] = pw

for _ in range(M):
    C = input().strip()
    print(f"{site_dict[C]}")