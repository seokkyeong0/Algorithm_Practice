N = int(input())

cp_area = [[0 for col in range(100)] for row in range(100)]
for i in range(N):
    A, B = map(int, input().split())
    if A <= 90 and B <= 90:
        for row in range(A, 10+A):
            for col in range(B, 10+B):
                cp_area[row][col] = 1
    elif A > 90 and B <= 90:
        for row in range(A, 100):
            for col in range(B, 10+B):
                cp_area[row][col] = 1
    elif A <= 90 and B > 90:
        for row in range(A, 10+A):
            for col in range(B, 100):
                cp_area[row][col] = 1
    else:
        for row in range(A, 100):
            for col in range(B, 100):
                cp_area[row][col] = 1

cp_cnt = 0
for i in range(100):
    for j in range(100):
        if cp_area[i][j] == 1:
            cp_cnt += 1
print(f"{cp_cnt}")