N = int(input())
array = []

temp = input().split()
for i in range(N):
    array.append(int(temp[i]))
array.sort()

M = int(input())
data = []

temp2 = input().split()
for i in range(M):
    data.append(int(temp2[i]))

for i in range(M):
    search = data[i]
    low_index, high_index = 0, N-1
    is_find = False

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        if array[mid_index] < search:
            low_index = mid_index + 1
        elif array[mid_index] > search:
            high_index = mid_index - 1
        else:
            print(1)
            is_find = True
            break
    if not is_find:
        print(0)