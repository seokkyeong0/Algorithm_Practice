num_list = []
for i in range(5):
    num_list.append(int(input()))

temp = 0
for i in range(5):
    for j in range(4-i):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j+1]
            num_list[j+1] = num_list[j]
            num_list[j] = temp

n_sum = 0
for num in num_list:
    n_sum += num
print(f"{n_sum / 5:.0f}")
print(f"{num_list[2]}")