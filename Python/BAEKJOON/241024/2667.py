from collections import deque


def bfs(y, x, n, cnt):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        yi, xj = q.popleft()
        cnt += 1
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = yi + di, xj + dj
            if 0 <= ni < n and 0 <= nj < n and maps[ni][nj] == '1' and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return cnt


N = int(input())
maps = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
apartments = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == '1' and not visited[i][j]:
            apartments.append(bfs(i, j, N, 0))
apartments.sort()
print(len(apartments))
for apartment in apartments:
    print(apartment)