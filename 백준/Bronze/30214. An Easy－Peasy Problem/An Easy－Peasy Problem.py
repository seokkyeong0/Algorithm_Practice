def diff(s1, s2):
    if s2 / 2.0 <= s1:
        return "E"
    else:
        return "H"

s1, s2 = map(int, input().split())
print(diff(s1, s2))