# deque 활용
from collections import deque

# 컨베이어 벨트 하나의 길이 N과 내구도 점검 기준이 되는 값 K
N, K = map(int, input().split())
# 벨트 내구도 정보를 입력 받고
belt = deque(map(int, input().split()))
# 로봇 위치 정보를 저장할 배열 robots
robots = deque([False]*N)
# 단계를 저장할 변수 level
level = 1
# while문
# 전체 공정은 컨베이어 벨트 회전, 로봇 이동, 로봇 올리기, 내구도 검사로 이루어짐
while True:
    # 컨베이어 벨트 회전
    # 제일 끝 값을 제일 처음으로 넣어준다.
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())
    # 회전 후 로봇이 내리는 위치 도달하면 내리기
    if robots[N-1]:
        robots[N-1] = False
    # 로봇 이동
    # 이때 가장 먼저 올린 로봇부터 이동하므로 위쪽 컨베이어 밸트의 제일 오른쪽 위치한 로봇부터 이동
    for i in range(N-1):
        # 로봇이 있고 한 칸 오른쪽에 밸트의 내구도가 존재하고, 로봇이 존재하지 않는다면
        if robots[N-2-i] and belt[N-1-i] and not robots[N-1-i]:
            # 현재 위치에서 로봇을 제거
            robots[N-2-i] = False
            # 맨 처음 인덱스인 0일 때는 이동하면 바로 로봇을 내릴 수 있으므로
            # 맨 처음인 경우를 제외하고 이동할 새로운 위치에 로봇을 표시
            if i:
                robots[N-1-i] = True
            # 이동한 후에는 내구도를 1 감소
            belt[N-1-
                 i] -= 1
    # 로봇 올리기
    # 올리는 위치에 내구도가 여전히 존재한다면
    if belt[0]:
        # 해당 위치에 로봇을 올리고 내구도를 1 감소
        robots[0] = True
        belt[0] -= 1
    # 내구도 검사
    # 만약 밸트 전체에서 내구도가 0인 값이 K개 이상이면
    if belt.count(0) >= K:
        # 종료
        break
    # 그게 아니라면 다음 단계로 이동
    level += 1
print(level)