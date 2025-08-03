import sys
# sys.stdin.readline().rstrip()

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f"{A+B}")