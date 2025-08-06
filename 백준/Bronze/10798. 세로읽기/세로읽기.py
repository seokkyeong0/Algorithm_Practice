temp = [None] * 5
for i in range(5):
    num_list = list(input())
    temp[i] = num_list

for i in range(15):
    for j in range(5):
        try:
            if temp[j][i] != " " or temp[j][i] != None:
                print(f"{temp[j][i]}", end="")
            else:
                continue
        except:
            continue