N = int(input())
num_list = list(map(int, input().split()))

is_prime = True
cnt = 0
for i in range(len(num_list)):
    if num_list[i] == 0 or num_list[i] == 1:
        continue
    if num_list[i] >= 2:
        for k in range(2, num_list[i]):
            if num_list[i] % k == 0:
                is_prime = False
                break
    if is_prime:
        cnt += 1
    is_prime = True
print(f"{cnt}")