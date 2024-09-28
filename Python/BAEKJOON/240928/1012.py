import sys
from collections import deque


def bfs(y, x, m, n):
    q = deque()
    q.append((y, x))
    # 델타를 통해서 다른 배추를 찾아감
    while q:
        i, j = q.popleft()
        field[i][j] = 2
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = i+di, j+dj
            # 이동할 위치가 배열 안에 있고 배추가 안 심겨 있거나 이미 방문한 곳이 아닌 경우에만 방문
            if 0<=ni<m and 0<=nj<n and field[ni][nj] != 0 and field[ni][nj] != 2:
                q.append((ni, nj))
    return True


# 테스트 케이스 수 입력
T = int(input())
# 테스트 케이스 별 시행
for _ in range(T):
    # 그냥 M을 세로, N을 가로, K를 개수로 생각함
    M, N, K = map(int, sys.stdin.readline().split())
    # 밭의 배열을 만들고
    field = [[0]*N for _ in range(M)]
    # 배추의 위치를 입력
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    # 배추 벌레의 개수를 저장할 변수 cnt
    cnt = 0
    # 배열 전체를 순회하며
    for i in range(M):
        for j in range(N):
            if field[i][j] == 0 or field[i][j] == 2:
                continue
            bfs(i, j, M, N)
            cnt += 1

    # 모든 반복이 끝나고 cnt를 출력
    print(cnt)