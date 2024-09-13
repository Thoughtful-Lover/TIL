def mining(current_x, row, column, land):
    global sub_sum
    sub_sum = 0
    visited = [[0] * column for _ in range(row)]
    for j in range(row):
        if land[j][current_x] == 0:
            continue
        dfs(j, current_x, row, column, land, 1)

def dfs(y, x, r, c, land, cnt):
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni, nj = y+di, x+dj
        if 0<=ni<r and 0<=nj<c and not visited[ni][nj] and land[ni][nj] == 1:
            visited[ni][nj] = 1



def solution(land):
    n = len(land)
    m = len(land[0])
    answer = 0
    for i in range(m):
        mining(i, n, m, land)
    return answer