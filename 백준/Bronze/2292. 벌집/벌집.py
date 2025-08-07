N = int(input())

pre_min = 2
pre_max = 7
total_floor = 0
for i in range(1, 18258):
    if pre_min <= N <= pre_max:
        total_floor = (6 * (i+1)) // 6
    if total_floor != 0:
        break
    pre_min += (6 * i)
    pre_max += (6 * (i+1))
        
if N == 1:
    print(f"{1}")
else:
    print(total_floor)