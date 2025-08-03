student = list(0 for i in range(28))
badguy = []

for i in range(len(student)):
    student[i] = int(input())

for i in range(1, 31):
    if not(i in student):
        badguy.append(i)
        
if badguy[0] > badguy[1]:
    print(f"{badguy[1]}")
    print(f"{badguy[0]}")
else:
    print(f"{badguy[0]}")
    print(f"{badguy[1]}")