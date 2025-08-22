is_end = False
while not(is_end):
    N = int(input())

    if N == 0:
        is_end = True
        break
        
    is_prime = [True] * (2*N+2)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(((2*N+1)**0.5)+1)):
        if is_prime[i]:
            for j in range(i*i, 2*N+2, i):
                is_prime[j] = False

    cnt = 0
    for num in range(N+1, 2*N+1):
        if is_prime[num]:
            cnt += 1
    print(cnt)