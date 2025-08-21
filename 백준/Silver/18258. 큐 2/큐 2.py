import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
out = []

for _ in range(N):
    cv = input().split()

    if cv[0] == "push":
        queue.append(int(cv[1]))
    elif cv[0] == "pop":
        if queue:
            out.append(str(queue.popleft()))
        else:
            out.append("-1")
    elif cv[0] == "size":
        out.append(str(len(queue)))
    elif cv[0] == "empty":
        out.append("0" if queue else "1")
    elif cv[0] == "front":
        out.append(str(queue[0]) if queue else "-1")
    elif cv[0] == "back":
        out.append(str(queue[-1]) if queue else "-1")

print("\n".join(out))