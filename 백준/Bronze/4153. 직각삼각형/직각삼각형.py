while True:
    M = list(map(int, input().split()))
    M.sort()
    if M[0] == 0 and M[1] == 0 and M[2] == 0:
        break
    else:
        if M[0]**2 + M[1]**2 == M[2]**2:
            print(f"right", end="\n")
        else:
            print(f"wrong", end="\n")