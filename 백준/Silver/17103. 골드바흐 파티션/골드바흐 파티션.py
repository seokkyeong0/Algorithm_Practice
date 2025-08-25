T = int(input())

is_prime = [True] * (1000000 + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(1000000**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, 1000000+1, i):
            is_prime[j] = False

for _ in range(T):
    N = int(input())
    cnt = 0
    for p in range(2, N // 2 + 1):
        if is_prime[p] and is_prime[N - p]:
            cnt += 1
    print(f"{cnt}")