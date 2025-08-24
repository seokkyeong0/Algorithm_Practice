while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    else:
        print(f"{M+F}")