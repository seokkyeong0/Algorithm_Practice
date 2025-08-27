from collections import deque

N = int(input())
n_list = list(map(int, input().split()))

dq = deque((i+1, n_list[i]) for i in range(N))
out = []

while dq:
    idx, move = dq.popleft()
    out.append(str(idx))

    if not dq:
        break

    if move > 0:  # 오른쪽 이동
        for _ in range(move - 1):
            dq.append(dq.popleft())
    else:         # 왼쪽 이동
        for _ in range(abs(move)):
            dq.appendleft(dq.pop())

print(" ".join(out))