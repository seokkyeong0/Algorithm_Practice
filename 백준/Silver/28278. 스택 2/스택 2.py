import sys
input = sys.stdin.readline

N = int(input())
stack = []
out = []

for _ in range(N):
    C = input().split()
    if C[0] == "1":
        stack.append(int(C[1]))
    elif C[0] == "2":
        if len(stack) != 0:
            out.append(str(stack.pop()))
        else:
            out.append("-1")
    elif C[0] == "3":
        out.append(str(len(stack)))
    elif C[0] == "4":
        if len(stack) != 0:
            out.append("0")
        else:
            out.append("1")
    elif C[0] == "5":
        if len(stack) != 0:
            out.append(str(stack[-1]))
        else:
            out.append("-1")

print("\n".join(out))