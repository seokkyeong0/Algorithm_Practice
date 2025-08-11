while True:
    N = int(input())
    num_list = []
    n_sum = 0

    if N == -1:
        break
    
    for i in range(1,N+1):
        if N % i == 0 and i < N:
            num_list.append(i)
            
    for i in range(len(num_list)):
        n_sum += num_list[i]

    if N == n_sum:
        print(f"{N} = ", end = "")
        for num in num_list:
            print(f"{num}", end = "")
            if num == num_list[-1]:
                break
            print(f" + ", end = "")
        print()
    else:
        print(f"{N} is NOT perfect.")