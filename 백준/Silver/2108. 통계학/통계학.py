import sys
input = sys.stdin.readline

def myround(num):
    if num >= 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)
        
N = int(input())

n_list = []
count = [0] * 8001
for _ in range(N):
    num = int(input())
    n_list.append(num)
    count[num + 4000] += 1
n_list.sort()

max_freq = max(count)
modes = [i - 4000 for i, c in enumerate(count) if c == max_freq]
modes.sort()

print(f"{myround(sum(n_list) / len(n_list))}")
print(f"{n_list[myround(len(n_list) / 2) - 1]}")
print(f"{modes[1] if len(modes) > 1 else modes[0]}")
print(f"{n_list[-1] - n_list[0]}")