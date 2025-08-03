N = int(input())
score = list(map(int, input().split()))
max = score[0]
sum = 0

for i in score:
    if max < i:
        max = i
for i in range(len(score)):
    score[i] = (score[i]/max)*100
for i in range(len(score)):
    sum += score[i]
    
print(f"{sum / (len(score))}")