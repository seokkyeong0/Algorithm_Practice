S = input()

for ch in S:
    if ord(ch) < 97:
        print(f"{chr(ord(ch) + 32)}", end="")
    else:
        print(f"{chr(ord(ch) - 32)}", end="")