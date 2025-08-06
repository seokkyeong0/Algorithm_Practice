temp_A = [0] * 9
for i in range(9):
    num_list_A = list(map(int, input().split()))
    temp_A[i] = num_list_A

max_value = temp_A[0][0]
row_index = 1;
col_index = 1;

for i in range(9):
    for j in range(9):
        if max_value < temp_A[i][j]:
            max_value = temp_A[i][j]
            row_index = i+1
            col_index = j+1

print(f"{max_value}", end="\n")
print(f"{row_index} {col_index}")