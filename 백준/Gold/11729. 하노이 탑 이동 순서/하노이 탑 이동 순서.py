import sys
input = sys.stdin.readline
write = sys.stdout.write

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        write(f"{from_pos} {to_pos}\n")
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)
    write(f"{from_pos} {to_pos}\n")
    hanoi(n-1, aux_pos, to_pos, from_pos)

N = int(input())
write(f"{2**N - 1}\n")
hanoi(N, 1, 3, 2)