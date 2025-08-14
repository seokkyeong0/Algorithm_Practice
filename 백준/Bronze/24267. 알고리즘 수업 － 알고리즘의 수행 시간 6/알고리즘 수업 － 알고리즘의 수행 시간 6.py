n = int(input())

temp = 1
n_sum = 3
for i in range(3,n):
    temp += n_sum
    n_sum += i

if n < 3:
    print(0, 3, sep = "\n")
else:
    print(temp, 3, sep = "\n")