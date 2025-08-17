N = int(input())
n_list = list(map(int, input().split()))

print(f"{min(n_list) * max(n_list)}")