M = int(input())
N = int(input())

num_sum = 0
num_list = []

for num in range(M, N+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        num_sum += num
        num_list.append(num)

if num_list:
    print(num_sum)
    print(num_list[0])
else:
    print(-1)