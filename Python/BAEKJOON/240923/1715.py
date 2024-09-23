'''
1715. 카드 정렬하기

두 카드 묶음을 정렬하는데
예컨대 두 개의 묶음을 A, B라 할 때
A+B번 비교를 통해 정렬해야 돼 !

최소한의 비교 횟수로 정렬을 하는 법은?

첫째 줄에 N (1<=N<=100,000)
N개의 줄에 걸쳐 숫자 카드 묶음 각각의 크기 (0<=<1,000, 양의 정수)
'''

# 제일 작은 개수의 카드 뭉치들을 계속해서 비교해야 됨
# 근데 최소인 값들만 비교를 해가야하기 때문에 heap을 이용할거임
import heapq as hq


# n을 입력 받음
n = int(input())
# 카드들의 개수를 저장할 빈 배열 cards
cards = []
# 값들을 heappush
for _ in range(n):
    hq.heappush(cards, int(input()))
# 비교횟수를 저장할 변수 cnt
cnt = 0
# 카드 뭉치가 하나만 남을 때까지
while len(cards) > 1:
    # 제일 작은 2개 값을 뽑아서
    A = hq.heappop(cards)
    B = hq.heappop(cards)
    # 비교해주고
    cnt += A+B
    # 뭉친 카드 뭉치를 다시 heapq에 넣어줌
    hq.heappush(cards, A+B)
# 위 과정을 마치면 비교횟수를 출력
print(cnt)