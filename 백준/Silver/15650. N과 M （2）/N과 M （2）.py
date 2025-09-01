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
            if len(sequence) == 0:
                visited[i] = True
                sequence.append(i)
            else:
                if i > sequence[-1]:
                    visited[i] = True
                    sequence.append(i)
                else:
                    continue

            # 재귀 호출
            backtrack()

            # 호출 종료 후 pop
            sequence.pop()
            visited[i] = False
backtrack()