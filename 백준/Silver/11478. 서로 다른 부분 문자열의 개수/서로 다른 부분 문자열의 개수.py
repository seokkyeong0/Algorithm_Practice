S = input()
T = set()
for i in range(len(S)):
    for j in range(len(S)-i):
        T.add(S[j:j+i+1])
print(len(T))