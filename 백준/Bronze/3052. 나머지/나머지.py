num = list(0 for i in range(10))
for i in range(len(num)):
    num[i] = int(input())
comp = list(0 for i in range(10))
for i in range(10):
    comp[i] = num[i] % 42

comp.sort()
count = 1
for i in range(len(comp)-1):
    if comp[i] != comp[i+1]:
        count += 1
print(f"{count}")