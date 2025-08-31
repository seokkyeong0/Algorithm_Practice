N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(input())

min_cnt = 0
while K > 0:
    for i in range(len(coin)):
        if K < int(coin[-(i+1)]):
            continue
        else:
            min_cnt += (K // int(coin[-(i+1)]))
            K %= int(coin[-(i+1)])
            break
print(f"{min_cnt}")