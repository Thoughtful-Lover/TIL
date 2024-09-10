# R, C, K 행, 열, 거리
# T는 못감
# 한 번 간 곳은 안감
# 주어진 거리만큼 걸렸을 때의 가짓수를 출력


# 매개변수 앞에서부터 순서댈로 현재 y좌표, 현재 x좌표, 현재까지의 거리, 열의 길이, 행의 길이, 목표 길이
def dfs(current_y, current_x, current_dist, r, c, k):
    # 글로벌 변수 cnt를 호출
    global cnt
    # 만약 목표 위치에 도달 했다면
    if current_y == 0 and current_x == c-1:
        # 현재까지의 거리가 목표 거리와 일치할 때
        if current_dist == k:
            # cnt를 1 증가
            cnt += 1
        # 그리고 함수를 종료
        return
    # 델타로 이동
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        # 현재 값에서 이동할 위치의 값을 계산하고
        ni, nj = current_y+di, current_x+dj
        # 두 값이 도로의 인덱스 상에 위치하고 앞으로 이동할 값이 벽이 아니고, 아직 방문하지 않았을 때
        if 0<=ni<r and 0<=nj<c and roads[ni][nj] != 'T' and not visited[ni][nj]:
            # 방문 표시를 하고
            visited[ni][nj] = 1
            # 이동. 이동할 위치의 좌표와 거리+1, 나머지 행, 열, 목표 거리 정보는 동일
            dfs(ni, nj, current_dist+1, r, c, k)
            # 함수 호출이 끝나면 안 방문한걸로 다시 표시
            visited[ni][nj] = 0


# 열의 길이 R, 행의 길이 C, 목표 거리 K
R, C, K = map(int, input().split())
# 도로의 정보를 배열 roads에 저장
roads = [list(input()) for _ in range(R)]
# 방문한 위치를 저장해줄 배열 visited
visited = [[0]*C for _ in range(R)]
# 거리가 일치하는 만큼 개수를 세줄 변수 cnt
cnt = 0
# 시작 위치에 방문 표시
visited[R-1][0] = 1
# 함수 호출
dfs(R-1, 0, 1, R, C, K)
# 함수 호출이 끝나고 바뀐 cnt 값을 출력
print(cnt)