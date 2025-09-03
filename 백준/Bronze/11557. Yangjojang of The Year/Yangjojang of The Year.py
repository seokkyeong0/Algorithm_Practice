T = int(input())

for _ in range(T):
    ua_dict = {}
    N = int(input())
    for _ in range(N):
        U, A = input().split()
        ua_dict[U] = int(A)
    ua_dict = dict(sorted(ua_dict.items(), key = lambda x: x[1], reverse=True))
    print(next(iter(ua_dict)))