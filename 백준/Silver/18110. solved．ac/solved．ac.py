import sys
input = sys.stdin.readline

def Roundup(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
div = Roundup(N * 15 / 100)

d_list = []
for _ in range(N):
    d_list.append(int(input()))
d_list.sort()

total = 0
for _ in range(Roundup(div), N - Roundup(div)):
    total += d_list[_]

if N != 0:
    print(f"{Roundup(total / (N - (div * 2)))}")
else:
    print(f"{0}")