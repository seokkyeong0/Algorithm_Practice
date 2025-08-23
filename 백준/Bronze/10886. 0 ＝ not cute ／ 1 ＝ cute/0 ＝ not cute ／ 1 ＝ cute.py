N = int(input())

pros = 0
cons = 0
for _ in range(N):
    O = int(input())
    if O == 0:
        cons += 1
    elif O == 1:
        pros += 1
        
if pros > cons:
    print(f"Junhee is cute!")
else:
    print(f"Junhee is not cute!")