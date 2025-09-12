N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
temp = 0
is_min = False
for i in range(len(price)-1):
    if is_min:
        total += temp * road[i]
        if temp > price[i+1]:
            is_min = False
    else:
        if price[i] < price[i+1]:
            total += price[i] * road[i]
            temp = price[i]
            is_min = True
        else:
            total += price[i] * road[i]
print(f"{total}")