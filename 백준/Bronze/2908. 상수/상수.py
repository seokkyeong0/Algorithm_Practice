A, B = input().split()
list_A = [] 
list_B = []

for i in range(3,0,-1):
    list_A.append(A[i-1])
    list_B.append(B[i-1])

num_A = int(list_A[0]) * 100 + int(list_A[1]) * 10 + int(list_A[2]) * 1
num_B = int(list_B[0]) * 100 + int(list_B[1]) * 10 + int(list_B[2]) * 1

if num_A > num_B:
    print(f"{num_A}")
else:
    print(f"{num_B}")