N = int(input())

num_list = []
div = 2
while N > 1:
    if N / div != int(N / div):
        div += 1
    else:
        N /= div
        num_list.append(div)
for num in num_list:
    print(f"{num}")