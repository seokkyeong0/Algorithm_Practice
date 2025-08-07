upper = list(chr(i+65) for i in range(26))
lower = list(chr(i+97) for i in range(26))

S = input()
temp = [0] * 26
max_chr = temp[0]
curr_chr = ""

for i in range(len(S)):
    for j in range(26):
        if S[i] == lower[j]:
            temp[j] += 1
        if S[i] == upper[j]:
            temp[j] += 1

temp_index = 0
for i in range(26):
    if max_chr < temp[i]:
        max_chr = temp[i]
        temp_index = i

is_same = False
for i in range(temp_index, 25):
    if max_chr == temp[i+1]:
        is_same = True
        
if is_same:
    print(f"?")
else:
    print(f"{upper[temp_index]}")