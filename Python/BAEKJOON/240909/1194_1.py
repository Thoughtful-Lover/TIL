from collections import deque

def bfs(start_y, start_x, n, m):
    global cnt
    q = deque()
    visited = [[False]*m for _ in range(n)]
    visited_keys = deque()
    q.append([start_y, start_x, 0, 0, 0, 0, 0, 0, 0])
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
                elif (maze[ni][nj] == '.' or maze[ni][nj] == '0') and not visited[ni][nj]:
                    visited[ni][nj] = True
                    current_node[2] += 1
                    q.append([current_node[0], current_node[1], current_node[2], current_node[3], current_node[4], current_node[5], current_node[6], current_node[7], current_node[8]])
                # a, f, A, F = 97, 102, 65, 70
                elif 97<=ord(maze[ni][nj])<=102 and not visited[ni][nj]:
                    visited = [[False]*M for _ in range(N)]
                    visited_keys.append((ni, nj))
                    for visited_key in visited_keys:
                        visited[visited_key[0]][visited_key[1]] = True
                    current_node[2] += 1
                    current_node[ord(maze[ni][nj])-94] = 1
                    q.append([current_node[0], current_node[1], current_node[2], current_node[3], current_node[4], current_node[5], current_node[6], current_node[7], current_node[8]])
                elif 65 <= ord(maze[ni][nj]) <= 70 and not visited[ni][nj] and current_node[ord(maze[ni][nj])-94]:
                    visited[ni][nj] = True
                    current_node[2] += 1
                    q.append([current_node[0], current_node[1], current_node[2], current_node[3], current_node[4], current_node[5], current_node[6], current_node[7], current_node[8]])

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
keys = [0]*6
cnt = -1
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            bfs(i, j, N, M)
            break
print(cnt)