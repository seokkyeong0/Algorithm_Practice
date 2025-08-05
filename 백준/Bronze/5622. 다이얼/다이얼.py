A = input()
req_time = 0
for _ in range(len(A)): 
    if 65 <= ord(A[_]) < 80:
        req_time += (3 + ((ord(A[_]) % 65) // 3))
    if 80 <= ord(A[_]) < 84:
        req_time += 8
    if 84 <= ord(A[_]) < 87:
        req_time += 9
    if 87 <= ord(A[_]):
        req_time += 10
print(f"{req_time}")