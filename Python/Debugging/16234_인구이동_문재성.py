'''
NxN 크기의 땅
각각의 땅 = 나라
인구 이동은 아래 방법에 의해 인구 이동이 없을 때까지 지속
0) day += 1
1) L명 이상 R명 이하의 인구 수 차이가 나면, 국경선 개방
2) 국경선이 서로 열려있으면 연합
3) 연합을 이루고 있는 각 나라의 인구수는 (연합의 인구수)//(연합을 이루고 있는 칸의 개수)
4) 연합 해체
'''

from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cnt = 0
day = 0
while True:     # 반복 시켜
    visited = [[0] * N for _ in range(N)]   # bfs 위해 visited
    germans = {}    # 연합을 key로 : 인구이동 후의 인구수 = (연합의 인구수)//(연합을 이루고 있는 나라의 수) 를 value로
    for i in range(N):
        for j in range(N):
            q = deque()     # bfs 위한 deque
            union = []  # 연합의 좌표(i, j)를 넣을 리스트
            if not visited[i][j]:   # 해당 칸을 방문하지 않았으면,
                q.append((i, j))    # 큐에 넣고
                union.append((i, j))    # 연합에도 넣고
                visited[i][j] = 1   # 방문 처리를 한다
                cnt = 1     # 연합국의 수
                sum = arr[i][j]     # 연합의 인구수 초기설정
                while q:
                    (i, j) = q.popleft()    # 큐에서 빼내서
                    for k in range(4):      # 4방향 탐색
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if not visited[ni][nj]:     # ni, nj 방문 안되었을 때,
                                if L <= abs(arr[i][j] - arr[ni][nj]) <= R:  # 국경선 개방 가능하면
                                    q.append((ni, nj))      # 큐에 넣고
                                    union.append((ni, nj))  # 연합에도 넣고
                                    visited[ni][nj] = 1  # ni, nj 방문처리 하고
                                    sum += arr[ni][nj]  # 연합 인구수 증가시키고
                                    cnt += 1    # 연합국의 수도 증가시킴
                if cnt > 1:     # 연합국이 2이상일 경우에만 연합임
                    # 연합을 key로 : 인구이동 후의 인구수 = (연합 인구수)//(연합국의 수) 를 value 로
                    germans[tuple(union)] = sum // cnt

    if germans:     # 연합이 하나라도 있으면
        day += 1    # 인구이동 -> 날짜 하나 증가시키고
        for union in germans.keys():    # 연합을 하나씩 빼서
            for (i, j) in union:    # 연합을 이루는 좌표를 빼서
                arr[i][j] = germans[union]  # 인구이동 시킴
    else:   # 연합이 없으면 끝
        break

print(day)