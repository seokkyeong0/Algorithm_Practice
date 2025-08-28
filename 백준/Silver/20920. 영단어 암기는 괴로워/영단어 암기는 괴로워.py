import sys
input = sys.stdin.readline

N, M = map(int, input().split())

w_dict = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in w_dict:
            w_dict[word] += 1
        else:
            w_dict[word] = 1

my_dict = sorted(w_dict.keys(), key=lambda x: (-w_dict[x], -len(x), x))
print("\n".join(my_dict))