def star(N):
    if N == 3:
        return ["***", "* *", "***"]
        
    small = star(N//3)
    result = []
    
    for line in small:
        result.append(line*3)
    for line in small:
        result.append(line + " "*(N//3) + line)
    for line in small:
        result.append(line*3)
    return result

N = int(input())
result = star(N)
for i in range(N):
    print("".join(result[i]))