S = input()
word = 0

for i in range(len(S)):
    if S[i] == " ":
        word += 1
if S[0] != " ":
    word += 1
if S[-1] == " ":
    word -= 1

print(f"{word}")