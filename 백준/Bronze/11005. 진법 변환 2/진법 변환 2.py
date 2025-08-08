N, B = map(int, input().split())
total = []
temp = N
while temp > 0:
    total.append(temp % B)
    temp = int(temp / B)

for i in range(len(total)):
    if total[-(i+1)] > 9:
        print(f"{chr(total[-(i+1)] + 55)}", end="")
    if total[-(i+1)] < 10:
        print(f"{total[-(i+1)]}", end="")