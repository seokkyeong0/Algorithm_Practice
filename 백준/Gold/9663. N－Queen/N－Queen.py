def solve(row, cols, diag1, diag2):
    if row == N:
        return 1
    count = 0
    avail = ((1 << N) - 1) & ~(cols | diag1 | diag2)
    while avail:
        pos = avail & -avail
        avail -= pos
        count += solve(row + 1,
                        cols | pos,
                        (diag1 | pos) << 1,
                        (diag2 | pos) >> 1)
    return count

def nqueen(N):
    limit = N // 2
    count = 0

    for col in range(limit):
        pos = 1 << col
        count += solve(1, pos, pos << 1, pos >> 1) * 2

    if N % 2:
        col = limit
        pos = 1 << col
        count += solve(1, pos, pos << 1, pos >> 1)

    return count

N = int(input())
print(nqueen(N))