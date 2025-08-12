while True:
    l_list = list(map(int, input().split()))
    l_list.sort()
    if l_list[0] == l_list[1] == l_list[2] == 0:
        break
        
    if l_list[-1] < l_list[0] + l_list[1]:
        if l_list[0] == l_list[1] == l_list[2]:
            print(f"Equilateral")
        elif l_list[0] == l_list[1]:
            print(f"Isosceles")
        elif l_list[1] == l_list[2]:
            print(f"Isosceles")
        elif l_list[0] == l_list[2]:
            print(f"Isosceles")
        else:
            print(f"Scalene")
    else:
        print(f"Invalid")