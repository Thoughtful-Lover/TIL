from collections import deque

def solution(land):
    def mining(y, x):
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = y+di, x+dj
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and land[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                mining(ni, nj)
    n = len(land)
    m = len(land[0])
    answer = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or land[i][j] > 1:
                continue
            q = deque([(i, j)])
            visited = [[0]*m for _ in range(n)]
            mining(i, j)
            v = len(q)
            checked = [0]*n
            while q:
                y, x = q.popleft()
                if not checked[y]:
                    checked[y] = 1
                    land[y][x] = v
    for i in range(m):
        sub_sum = 0
        for j in range(n):
            if land[j][i] > 1:
                sub_sum += land[j][i]
        if answer < sub_sum:
            answer = sub_sum
    return answer