# 힙큐를 import
from queue import PriorityQueue

# 테스트 케이스 수
T = int(input())
# 각 테스트 케이스별 시행
for _ in range(T):
    # 챕터의 개수 K
    K = int(input())
    # 챕터를 입력 받고
    chapters = list(map(int, input().split()))
    # 빈 우선순위 큐를 정의
    chapters_queue = PriorityQueue()
    # 챕터의 값들을 우선순위 큐 chapters_que에 넣어준다.
    for number in user_input.split():
        pq.put(int(number))
    # 합치는 비용을 저장해줄 변수 cost
    cost = 0
    # 합치는 값이 최소 2개일 때까지만 시행
    while chapters_queue.qsize() > 1:
      # 우선순위 큐에서 가장 작은 값 두 개를 빼고
      a = chapters_queue.get()
      b = chapters_queue.get()
      # 비용에 더해주고
      cost += (a+b)
      # 더한 값을 우선순위 큐에 다시 저장
      chapters_queue.put(a+b)
    # 위 시행을 모두 마치고 cost를 출력
    print(cost)