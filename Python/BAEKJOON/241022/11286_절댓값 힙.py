# 힙큐와 입력 방식을 활용
import heapq as hq
import sys

# 빈 배열 q를 정의
q = []
# 연산의 개수 N을 입력 받음
N = int(sys.stdin.readline())
# N회 만큼 연산 수행
for _ in range(N):
    # 정수 x를 입력 받음
    x = int(sys.stdin.readline())
    # x가 0일 때
    if not x:
        # q가 비어 있지 않으면
        if q:
            # 값을 하나 뽑아서
            v = hq.heappop(q)
            # 양의 정수이면
            if v[1]:
                # 그냥 출력
                print(v[0])
            # 음의 정수이면
            else:
                # -를 붙여서 출력
                print(-v[0])
        # 빈 배열이면 0을 출력
        else:
            print(0)
    # 만약 정수를 입력 받았다면
    else:
        # 양의 정수일 때
        if x > 0:
            # 해당 값과 True 값을 튜플로 추가
            hq.heappush(q, (x, True))
        # 음의 정수일 때
        else:
            # 해당 값의 - 값 (절대값) 과 False 값을 튜플로 추가
            hq.heappush(q, (x, False))