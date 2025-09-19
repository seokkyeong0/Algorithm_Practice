n = []
for _ in range(9):
    n.append(int(input()))

s = 0
for i in range(3):
    for a in range(i+1,9):
        for b in range(a+1,9):
            for c in range(b+1,9):
                for d in range(c+1,9):
                    for e in range(d+1,9):
                        for f in range(e+1,9):
                            s = n[i] + n[a] + n[b] + n[c] + n[d] + n[e] + n[f]
                            if s == 100:
                                print(f"{n[i]}")
                                print(f"{n[a]}")
                                print(f"{n[b]}")
                                print(f"{n[c]}")
                                print(f"{n[d]}")
                                print(f"{n[e]}")
                                print(f"{n[f]}")
                                quit()
                            else:
                                s = 0