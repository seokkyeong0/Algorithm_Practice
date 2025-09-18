def moose(x, y):
    if x == 0 and y == 0:
        print(f"Not a moose")
    elif x == y:
        print(f"Even {x+y}")
    elif x != y:
        print(f"Odd {x*2 if x > y else y*2}")

x, y = map(int, input().split())
moose(x, y)