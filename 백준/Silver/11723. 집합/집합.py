import sys

M = int(sys.stdin.readline())
S = 0
write = sys.stdout.write

for _ in range(M):
    cm = sys.stdin.readline().split()
    if cm[0] == "add":
        S |= 1 << int(cm[1])
    elif cm[0] == "remove":
        S &= ~(1 << int(cm[1]))
    elif cm[0] == "check":
        write("1\n" if S & (1 << int(cm[1])) else "0\n")
    elif cm[0] == "toggle":
        S ^= 1 << int(cm[1])
    elif cm[0] == "all":
        S = (1 << 21) - 1
    elif cm[0] == "empty":
        S = 0