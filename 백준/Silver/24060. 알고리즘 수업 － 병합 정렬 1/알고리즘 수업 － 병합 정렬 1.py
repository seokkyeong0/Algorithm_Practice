import sys
input = sys.stdin.readline

A, K = map(int, input().split())
n_list = list(map(int, input().split()))

count = 0
result = -1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

def merge(A, p, q, r):
    global count, result
    tmp = []
    i, j = p, q + 1

    # 두 배열을 비교하면서 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 왼쪽 배열 남은 것 처리
    while i <= q:
        tmp.append(A[i])
        i += 1

    # 오른쪽 배열 남은 것 처리
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 결과를 원래 배열에 복사
    for k in range(len(tmp)):
        A[p + k] = tmp[k]
        count += 1
        if count == K:
            result = A[p + k]

merge_sort(n_list, 0, A - 1)
print(result)