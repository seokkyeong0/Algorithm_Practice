N = int(input())
c_list = []

for d in range (1000000 + 1):
    d1 = d % 10 // 1
    d2 = d % 100 // 10
    d3 = d % 1000 // 100
    d4 = d % 10000 // 1000
    d5 = d % 100000 // 10000
    d6 = d % 1000000 // 100000
    d7 = d % 10000000 // 1000000

    if N == d + d1 + d2 + d3 + d4 + d5 + d6 + d7:
        c_list.append(d)
    else:
        continue

try:
    c_list.sort()
    print(f"{c_list[0]}")
except:
    print(f"{0}")