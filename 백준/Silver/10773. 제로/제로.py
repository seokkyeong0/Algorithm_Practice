K = int(input())

stack = []
for _ in range(K):
    S = int(input())

    if S == 0:
        stack.pop()
    else:
        stack.append(S)

print(sum(stack))