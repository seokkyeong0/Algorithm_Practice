S = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in range(len(alphabet)):
    if alphabet[i] in S:
        for j in range(len(S)):
            if S[j] == alphabet[i]:
                print(f"{j}", end=" ")
                break
    else:
        print(f"{-1}", end=" ")