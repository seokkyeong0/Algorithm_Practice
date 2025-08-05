N = int(input())
shirt_list = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_sum = 0
for i in range(len(shirt_list)):
    if (shirt_list[i] == 0):
        continue
    elif (shirt_list[i] // T) < 1:
        shirt_sum += 1
    elif (shirt_list[i] % T) == 0:
        shirt_sum += (shirt_list[i] // T)
    else:
        shirt_sum += (shirt_list[i] // T) + 1
        
print(shirt_sum)
print(f"{N//P} {N%P}")