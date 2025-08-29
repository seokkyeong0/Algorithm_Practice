def cantore(start, length, S):
    # 1. 종료 조건
    if length == 1:
        return

    # 2. 가운데 1/3 비우기
    mid = length // 3
    for i in range(start + mid, start + 2*mid):
        S[i] = " "

    # 3. 왼쪽 구간 재귀
    cantore(start, mid, S)

    # 4. 오른쪽 구간 재귀
    cantore(start + 2*mid, mid, S)

while True:
    try:
        N = int(input())
        S = ['-'] * (3**N)
        cantore(0, 3**N, S)
        print("".join(S))
    except EOFError:
        break