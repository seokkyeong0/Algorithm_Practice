L = int(input())
A = input()

hash_sum = 0
for i in range(L):
    hash_sum += (ord(A[i])-96)*(31**i)
print(f"{hash_sum % 1234567891}")