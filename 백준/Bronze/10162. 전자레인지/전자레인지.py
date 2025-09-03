T = int(input())

A = T // 300
T = T - (A*300) 
B = T // 60
T = T - (B * 60)
C = T // 10

if T % 10 == 0:
    print(f"{A} {B} {C}")
else:
    print(f"{-1}")