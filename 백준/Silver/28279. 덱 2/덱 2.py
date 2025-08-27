import sys
from collections import deque

input = sys.stdin.readline

dq = deque()
N = int(input())
out = []
for _ in range(N):
    cm = list(map(str, input().split()))
    if cm[0] == "1":
        dq.appendleft(cm[1])
    elif cm[0] == "2":
        dq.append(cm[1])
    elif cm[0] == "3":
        if len(dq) != 0:
            out.append(dq.popleft())
        else:
            out.append("-1")
    elif cm[0] == "4":
        if len(dq) != 0:
            out.append(dq.pop())
        else:
            out.append("-1")
    elif cm[0] == "5":
        out.append(str(len(dq)))
    elif cm[0] == "6":
        if len(dq) != 0:
            out.append("0")
        else:
            out.append("1")
    elif cm[0] == "7":
        if len(dq) != 0:
            out.append(str(dq[0]))
        else:
            out.append("-1")
    elif cm[0] == "8":
        if len(dq) != 0:
            out.append(str(dq[-1]))
        else:
            out.append("-1")
            
sys.stdout.write("\n".join(out))