N, A, B = map(int, input().split())

if (A < N+(B-N)):
    print(f"Bus")
elif (A > N+(B-N)):
    print(f"Subway")
elif (A == N+(B-N)):
    print(f"Anything")