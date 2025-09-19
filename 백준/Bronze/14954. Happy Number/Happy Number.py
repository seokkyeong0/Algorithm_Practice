N = input()

total = 0
flag = False
happy = True
while (happy):
    total = 0
    for num in N:
        if flag and N == "4":
            print(f"UNHAPPY")
            happy = False
        total += int(num)**2
    if total == 1:
        print(f"HAPPY")
        break
    N = str(total)
    flag = True