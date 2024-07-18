'''
19843. 수면 패턴

일주일에 자야 할 시간을 나타내는 정수 T와 민티가 평일 동안 잠든 횟수를 나타내는 정수 N이 주어진다.

다음 줄부터 N개의 줄에 민티가 잠든 시간이 주어진다.
각 줄에 D1, H1, D2, H2의 순서로 민티가 잠든 시각과 일어난 시각이 주어진다.
D1은 잠든 요일, H1은 잠든 시각, D2는 일어난 요일, H2는 일어난 시각을 의미한다.
요일은 Mon, Tue, Wed, Thu, Fri 중 하나이며, 각각 월요일, 화요일, 수요일, 목요일, 금요일을 의미한다.
시각은 0 이상 23 이하의 정수로 주어지며, 각각 0시부터 23시까지의 시각을 의미한다.

각 수면은 서로 겹치지 않지만, 민티가 일어났다가 바로 잠들 수 있기 때문에 한 수면의 잠든 시각과 다른 수면의 일어난 시각이 동일한 경우가 있을 수 있다.
수면의 시작과 끝은 항상 평일이며, 입력은 잠든 시각이 빠른 순으로 정렬된 상태로 주어진다. 민티가 평일 동안 잠을 아예 자지 않는 경우가 존재할 수 있음에 유의하라.
'''


# 요일별 가중치를 담은 딕셔너리 days를 정의
days = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4
    }

# 자야할 시간 T와, 잠 잔 횟수 N을 입력
T, N = map(int, input().split())
# 총 잔 시간을 저장할 변수 sleep
sleep = 0
# N번 만큼 자고
for _ in range(N):
    # 자기 시작한 요일과 시간, 깨어난 요일과 시간을 입력 받음
    D1, H1, D2, H2 = input().split()
    # 깨어난 요일과 시간에서 자기 시작한 요일과 시간을 빼서 sleep에 더해줌
    sleep += ((days[D2]*24+int(H2)) - (days[D1]*24+int(H1)))
# 만약 주말 내내 자도 목표만큼 잘 수 없으면 -1을 출력
if T-sleep > 48:
    print(-1)
# 더 잘 필요가 없으면 0을 출력
elif T < sleep:
    print(0)
# 나머지 경우는 자야할 시간에서 잔 시간을 빼주면 주말에 자야할 시간을 구할 수 있다.
else:
    print(T-sleep)