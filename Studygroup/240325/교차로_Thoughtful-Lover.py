'''
십자 모양 교차로, 상하좌우 방향으로 직진만 가능
경로가 겹치면 1초 쉬었다가 가야 됨
1초에 한대씩만 교차로 오른쪽에 차가 없을 때 통과 가능
i번째 정수는 i번째 차량이 교차로를 통과한 시간
또는 교차로를 통과하지 않는다면 -1을 출력
'''

from collections import deque


def traffic_police():
    time = 0
    while order:
        current = order.popleft()
        current[0] = time
        next = current
        current = order.popleft()


N = int(input())
cars = [deque() for _ in range(4)]
order = deque()
time = [-1]*N
for _ in range(N):
    s, position = map(input().split())
    order.append((s, position))
    cars[ord(position)-65].append(s)