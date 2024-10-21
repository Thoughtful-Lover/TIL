# 힙큐
import heapq as hq
# 빠른 입력
import sys

# 선수의 수 N명, 최종 가치를 확인할 K년
N, K = map(int, sys.stdin.readline().split())
# 총 11개의 포지션을 가지는 팀, 인덱스에 맞추기 위해 12개의 하위 배열을 가지는 2차원 배열 정의
players = [[] for _ in range(12)]
# 선수 정보 입력
for _ in range(N):
    # 포지션 P와 가치 W
    P, W = map(int, sys.stdin.readline().split())
    # 힙으로 입력, - 값으로 heappush하면 가장 가치가 높은 선수가 우선순위가 가장 높게 입력됨
    hq.heappush(players[P], -W)
# K년 간 시행
for _ in range(K):
  # 각 선수의 포지션을 순환하며
    for i in range(1, 12):
        # 만약 해당 포지션에 선수가 존재한다면
        if players[i]:
            # 해당 포지션 선수 중 가장 큰 값을 뽑아서
            player = hq.heappop(players[i])
            # 만약 해당 선수의 가치가 0보다 크면
            if player < 0:
              # 값을 1만큼 낮춰주고
              player += 1
            # 다시 값을 넣어줌
            hq.heappush(players[i], player)
# 선수 가치의 합을 저장할 변수 value_sum
value_sum = 0
for j in range(1, 12):
    # 해당 포지션에 선수가 존재한다면
    if players[j]:
        # 최대인 선수의 가치를 더해줌
        value_sum += players[j][0]
# 지금까지 -로 선수 가치를 처리해주었기 때문에 마지막에 출력할 때 양의 정수로 바꿔줌
print(-value_sum)