S = input()
try:
    if S[0] == "\"" and S[1] == "\"":
        print(f"CE")
    elif S[0] == "\"" and S[-1] == "\"":
        print(f"{S[1:-1]}")
    else:
        print(f"CE")
except:
    print(f"CE")