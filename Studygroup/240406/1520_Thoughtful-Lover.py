'''
1520. 내리막 길
'''


def road(current_i, current_j):
    global cnt

    if current_i == M-1 and current_j == N-1:
        cnt += 1
        return

    for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
        ni = current_i+di
        nj = current_j+dj
        if 0<=ni<M and 0<=nj<N and map[current_i][current_j] > map[ni][nj]:
            road(ni, nj)


M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
cnt = 0

road(0, 0)
print(cnt)