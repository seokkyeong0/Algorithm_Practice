arr = list(0 for i in range(9))
for i in range(9):
    arr[i] = int(input())
    
max = arr[0]
index = 0
for i in arr:
    if max < i:
        max = i
print(f"{max}")

for i in arr:
    index += 1
    if max == i:
        break
print(f"{index}")