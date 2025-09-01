N, M = map(int, input().split())

visited = [False] * (N + 1)
sequence = []

def backtrack():
    # 재귀 호출 후 조건을 만족하면 출력하고 return으로 종료
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(1, N + 1):
        # 중복 체크
        if not visited[i]:
            visited[i] = True
            sequence.append(i)

            # 재귀 호출
            backtrack()

            # 호출 종료 후 pop
            sequence.pop()
            visited[i] = False
backtrack()