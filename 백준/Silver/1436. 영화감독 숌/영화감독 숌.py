N = int(input())

cnt = 1
ch_cnt = 0
doom = 666

while cnt < N:
    doom += 1
    ch_cnt = 0
    for i in range(len(str(doom))):
        if str(doom)[i] != "6":
            ch_cnt = 0
        else:
            ch_cnt += 1
        if ch_cnt > 2:
            ch_cnt = 0
            cnt += 1
            break
print(f"{doom}")