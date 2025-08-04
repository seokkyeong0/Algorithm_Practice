S = input().strip()
word = 0

if S != "":
    for i in range(len(S)):
        if S[i] == " ":
            word += 1
    word += 1

print(word)