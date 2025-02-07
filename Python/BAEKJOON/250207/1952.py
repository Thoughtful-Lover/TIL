M, N = map(int, input().split())
graph = [[0]*N for _ in range(M)]
graph[0][0] = 1
cnt = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
y, x = (0, 0)
idx = 0
while True:
    ny, nx = y+delta[idx%4][0], x+delta[idx%4][1]
    if 0<=ny<M and 0<nx<N and not graph[ny][nx]:
        graph[ny][nx] = 1
        y, x = ny, nx
    # rotate 해야 되는데 rotate할 때 조건
    elif is_turned:
        break
    elif not is_turned:
        idx += 1
        is_turned = True
print(cnt)