N = list(input())

temp = 0
for i in range(len(N)):
    for j in range(len(N)-1-i):
        if int(N[j]) < int(N[j+1]):
            temp = N[j+1]
            N[j+1] = N[j]
            N[j] = temp
for num in N:
    print(f"{num}", end="")