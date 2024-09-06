'''
2178. 미로 탐색
N*M 크기의 배열로 표현되는 미로
미로에서 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
1,1에서 N,M의 위치로 갈 때 걸리는 최소 칸수
'''

# 시간초과
# 그래서 sys.stdin.readline() 으로 읽어봤는데도 시간초과,,,
# 백트래킹 ?
'''import sys


# 함수 정의 매개변수 y, x는 현재 위치, n, m은 미로의 길이, count는 지나친 칸의 수
def adventure(y, x, n, m, count):
    global min_cnt
    # 델타로 상, 하, 좌, 우로 이동
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni = y+di
        nj = x+dj
        # 만약 다음에 이동하려는 값이 목적지/도착지이면
        if ni == n-1 and nj == m-1:
            # min_cnt 값과 비교해서 값을 갱신
            if min_cnt == 0 or min_cnt > count+1:
                min_cnt = count+1
            # 현 위치에서 다른 곳을 거쳐서 목적지로 가는 경로면 더 길어지는 경로이므로 return해도 무방
            return
        # 만약 이동할 위치가 미로 안에 위치하고, 아직 방문 안했고, 길이라면
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and maze[ni][nj] == '1':
            # 방문 표시를 해주고
            visited[ni][nj] = 1
            # 재귀로 다음 위치로 이동
            adventure(ni, nj, n, m, count+1)
            # 재귀를 마치고 오면 방문 표시를 해제
            visited[ni][nj] = 0


# 세로 길이 N, 가로 길이 M
N, M = map(int, sys.stdin.readline().split())
# 미로를 2차원 배열로 구현, 이 때, 0, 1 값은 string임
maze = [list(sys.stdin.readline()) for _ in range(N)]
# 같은 곳으로 돌아 가지 않기 위해 방문한 곳을 표시하는 배열 visited
visited = [[0]*M for _ in range(N)]
# 지나야 하는 최소칸 수의 값을 저장할 변수 min_cnt
min_cnt = 0
# 출발점인 0, 0을 방문 표시
visited[0][0] = 1
# 함수 호출
adventure(0, 0, N, M,  1)
# 함수 수행의 결과로 갱신된 min_cnt 값을 출력
print(min_cnt)'''


# bfs 방식인걸 알고 코드를 그에 맞게 수정해 볼 것이다
import sys
from collections import deque


# 함수 정의 매개변수 n, m은 미로의 길이
def bfs(n, m):
    # 빈 데큐를 정의해주고
    q = deque()
    # 초기값으로 출발점을 저장해줌
    q.append((0, 0))
    # 데큐가 비어 있지 않는 동안
    while q:
        # 가장 최근에 입력한 값을 뽑아주고
        (y, x) = q.popleft()
        # 델타로 상, 하, 좌, 우로 이동
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni = y+di
            nj = x+dj
            # 만약 다음에 이동하려는 값이 목적지/도착지이면
            if ni == n-1 and nj == m-1:
                # 목적지의 값이 0이거나 현재 위치에서 이동하려는 값보다 크면 값을 갱신해주고 break
                # 왜냐하면 현재 위치에서 끝 점에 도달하게 되었다면 그 이외의 값으로 이동해봤자 더 오래 걸리게 됨
                if not visited[n-1][m-1] or visited[n-1][m-1] > visited[y][x]+1:
                    visited[n-1][m-1] = visited[y][x]+1
                break
            # 만약 이동할 위치가 미로 안에 위치하고, 아직 방문 안했고, 길이라면
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and maze[ni][nj] == '1':
                # 방문 표시를 현재까지 움직인 거리로 해주고 이 값을 q에 다시 넣어줌
                visited[ni][nj] = visited[y][x]+1
                q.append((ni, nj))


# 세로 길이 N, 가로 길이 M
N, M = map(int, sys.stdin.readline().split())
# 미로를 2차원 배열로 구현, 이 때, 0, 1 값은 string임
maze = [list(sys.stdin.readline()) for _ in range(N)]
# 방문한 곳에 현재까지 이동한 거리를 저장할 2차원 배열 visited
visited = [[0]*M for _ in range(N)]
# 출발점인 0, 0을 방문 표시
visited[0][0] = 1
# 함수 호출
bfs(N, M)
# 함수 수행의 결과로 저장된 이동의 최소값을 출력해준다.
print(visited[N-1][M-1])