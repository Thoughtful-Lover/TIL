from collections import deque

def bfs(start_y, start_x, n, m):
    global cnt
    q = deque()
    q.append([start_y, start_x, 1, 0, 0, 0, 0, 0, 0])
    while q:
        current_node = q.popleft()
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni = current_node[0] + di
            nj = current_node[1] + dj
            if 0<=ni<n and 0<=nj<m and maze[ni][nj] != '#':
                if maze[ni][nj] == '1':
                    if cnt == -1 or cnt > current_node[2]+1:
                        cnt = current_node[2]+1
                        continue
                elif maze[ni][nj] == '0' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    current_node[2] += 1
                    q.append(current_node)
                # a, f, A, F = 97, 102, 65, 70
                elif 97<=ord(maze[ni][nj])<=102 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    current_node[2] += 1
                    current_node[ord(maze[ni][nj])-94] = 1
                    q.append(current_node)
                elif 65 <= ord(maze[ni][nj]) <= 170 and not visited[ni][nj] and current_node[ord(maze[ni][nj])-62]:
                    visited[ni][nj] = True
                    current_node[2] += 1
                    q.append(current_node)

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
keys = [0]*6
visited = [[False]*M for _ in range(N)]
cnt = -1
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            bfs(i, j, N, M)
            break