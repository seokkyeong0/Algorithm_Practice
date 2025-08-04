T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    if int(R) >= len(S):
        for _ in range(int(R)):
            for i in range(int(R)):
                if _ < len(S):
                    print(f"{S[_]}", end="")
        print()
    else:
        for _ in range(len(S)):
            for i in range(int(R)):
                print(f"{S[_]}", end="")
        print()