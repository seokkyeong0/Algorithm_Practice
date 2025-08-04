list_n = list(map(int, input().split()))

if list_n == [1,2,3,4,5,6,7,8]:
    print(f"ascending")
elif list_n == [8,7,6,5,4,3,2,1]:
    print(f"descending")
else:
    print(f"mixed")