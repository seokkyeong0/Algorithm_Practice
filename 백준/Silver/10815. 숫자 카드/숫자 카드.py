N = int(input())
x = set(map(int, input().split()))

M = int(input())
y = list(map(int, input().split()))

result = [1 if num in x else 0 for num in y]
print(*result)