N = int(input())
mirror = [list(input()) for _ in range(N)]
K = int(input())
for i in range(N):
    if K == 1:
        for j in range(N):
            print(mirror[i][j], end='')
        print()
    elif K == 2:
        for j in range(1, N+1):
            print(mirror[i][-j], end='')
        print()
    elif K == 3:
        for j in range(N):
            print(mirror[-(i+1)][j], end='')
        print()