N, M = map(int, input().split())

A = set()
B = set()

num = list(map(int, input().split()))
for n in num:
    A.add(n)

num = list(map(int, input().split()))
for n in num:
    B.add(n)

A_B = set()
for a in A:
    if not(a in B):
        A_B.add(a)

B_A = set()
for b in B:
    if not(b in A):
        B_A.add(b)

print(f"{len(A_B) + len(B_A)}")