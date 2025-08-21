import sys
input = sys.stdin.readline

N = int(input())
stack = []
out = []

for _ in range(N):
    cv = input().split()
    
    if cv[0] == "push":
        stack.append(int(cv[1]))
    elif cv[0] == "pop":
        if stack:
            out.append(str(stack.pop()))
        else:
            out.append("-1")
    elif cv[0] == "size":
        out.append(str(len(stack)))
    elif cv[0] == "empty":
        out.append("0" if stack else "1")
    elif cv[0] == "top":
        if stack:
            out.append(str(stack[-1]))
        else:
            out.append("-1")

print("\n".join(out))