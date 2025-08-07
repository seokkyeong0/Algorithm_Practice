N, M = map(int, input().split())
C = list(map(int, input().split()))

max_c = 0
for i in range(len(C)):
    for j in range(len(C)):
        for k in range(len(C)):
            if i == j == k or i == j or j == k or i == k:
                continue
            else:
                if M >= C[i] + C[j] + C[k]:
                    if max_c < C[i] + C[j] + C[k]:
                        max_c = C[i] + C[j] + C[k]
print(max_c)