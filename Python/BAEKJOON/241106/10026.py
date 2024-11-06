import sys
sys.setrecursionlimit(10**6)

# 시작 위치 start_y, start_x, 전체 그림의 크기 n
def dfs(y, x, target, n):
    # 방문 표시를 해주고
    visited[y][x] = True
    # 델타로 이동
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni, nj = y + di, x + dj
        # 이동할 위치가 그림 안에 있고, 아직 방문 안했고, 이동할 위치에 있는 색깔이 시작 지점의 위치와 같다면
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and picture[ni][nj] == target:
                # 재귀
                dfs(ni, nj, target, n)


# 그림의 크기 N
N = int(input())
# 그림의 정보를 나타내는 2차원 배열 picture
picture = [list(input()) for _ in range(N)]
# 적록색약이 아닌 사람과 적록색약인 사람의 그림 내 위치의 확인 지점을 저장할 배열들
visited = [[False] * N for _ in range(N)]
# 적록색약이 아닌 사람과 적록색약인 사람이 보는 구역의 수를 저장할 변수들
cnt = 0
cnt_cb = 0
# 전체를 순회하며 각각의 방문 배열을 확인해 아직 방문 안했다면 함수 호출
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, picture[i][j], N)
            cnt += 1
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'R':
            picture[i][j] = 'G'
# visited 배열 초기화
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, picture[i][j], N)
            cnt_cb += 1
# 위의 반복문이 모두 종료되면 갱신된 값을 하나의 간격을 두고 출력
print(cnt, cnt_cb)