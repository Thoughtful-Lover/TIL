import sys
from collections import deque


# 보드의 길이 r,c
def dfs(r, c):
    # 글로벌 변수 cnt를 호출
    global cnt

    # q에 시작 위치와, 현재까지 완성된 문자열
    q = deque([[0, 0, ord(board[0][0])]])

    # 반복 진행
    while q:
        infos = q.popleft()

        # 기존 이동한 거리보다 많으면 값을 갱신
        if cnt < len(infos)-2:
            cnt = len(infos)-2

        # 델타로 이동
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            # 이동할 위치를 작성하고
            ni, nj = infos[0] + di, infos[1] + dj
            # 해당 값이 보드 위에 있고 아직 방문 안했으면
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj] not in infos:
                # 값을 넣어줌
                infos.append(ord(board[ni][nj]))
                q.append(infos)


# 행의 수 R과 열의 수 C를 입력 받음
R, C = map(int, sys.stdin.readline().split())
# 알파벳 보드의 정보를 입력
board = [list(sys.stdin.readline()) for _ in range(R)]
# 방문한 곳을 중복 방문하지 않기 위해 visited 배열을 만듬
# 말이 지나는 길이를 저장할 변수 cnt
cnt = 0
# ord('A') = 65
# 방문한 알파벳의 아스키 코드 값을 계산해서 이를 바탕으로 인덱싱해서 방문표시를 함
# 왼쪽 위에서 출발
dfs(R, C)
# 함수 호출이 끝나고 변한 값을 출력
print(cnt)