'''
maps는 n*m 크기의 게임 맵 정보 2차원 배열
n과 m은 각각 1 이상 100 이하의 자연수
n과 m은 서로 같을 수도 다를 수도 있지만 둘 모두 1인 경우는 주어지지 않음

maps는 0과 1로 이루어짐
0은 벽, 1은 길
처음에 캐릭터는 (1,1), 상대방 진영은 (n, m)

캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return
'''

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

# deque를 사용
from collections import deque


def solution(maps):
    # 초기값을 -1
    answer = -1
    # 배열의 세로 n과 가로 m을 각각 구함
    n = len(maps)
    m = len(maps[0])
    # 방문한 곳을 표시할 배열 visited를 정의
    visited = [[False]*m for _ in range(n)]
    # 시작 위치인 (1, 1)에 방문 표시. 리스트의 인덱스이므로 (0, 0)에 표시
    visited[0][0] = True
    # 초기 위치인 출발점과 지나간 거리 1을 포함한 deque를 정의
    q = deque([(0, 0, 1)])
    # 가보지 않은 모든 것을 다 갈 때까지
    while q:
        # 값을 하나 꺼내서, 현재의 y,x 위치, 현재까지의 거리로 설정
        current_y, current_x, current_dist = q.popleft()
        # 만약 상대 진영에 도착한 경우
        if current_y == n-1 and current_x == m-1:
            # 기존에 저장된 거리 값이 갱신되지 않았거나 현재 도착한 값보다 크면
            if answer == -1 or answer > current_dist:
                # 값을 갱신
                answer = current_dist
            # 아무튼 끝에 도착했다면 다음 값으로 넘어감
            continue
        # 델타로 상후좌우 방향으로 이동
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            # 이동할 위치 ni, nj
            ni, nj = current_y+di, current_x+dj
            # 이동할 위치가 배열 안에 위치하고 아직 방문한 적이 없고, 벽이 아니라 길이라면
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and maps[ni][nj]:
                # 이동할 위치와 거리를 새로 q에 넣음
                q.append((ni, nj, current_dist+1))
                # 그리고 방문 표시
                visited[ni][nj] = True
    # 위 과정을 모두 마치면 최소 거리나 -1을 출력
    return answer

# print(solution(maps))