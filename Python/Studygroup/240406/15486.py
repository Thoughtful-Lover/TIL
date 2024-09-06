'''
16486. 퇴사2

상담원 백준이는 퇴사
오늘부터 N+1일째 되는 날 퇴사하기 위해 N일 동안 최대한 많은 상담
매일 서로 다른 상담, 상담에 걸리는 시간 T와 받을 수 있는 금액 P

T시간짜리 상담 이후로는, T+1시간부터 일을 할 수 있고
N+1을 넘어서는 상담은 할 수 없다.
'''


def max_profit(working_days):
    start = 0
    profit = 0
    while True:
        start_profit = schedule[start][1]
        for j in range(start+1, start+schedule[start][0]):
            if j+schedule[j][0] > working_days:
                continue
            if schedule[j][1] > start_profit or j+

    return profit


N = int(input())
schedule = [0] * N
for i in range(N):
    (T, P) = map(int, input().split())
    schedule[i] = (T, P)
print(max_profit(N))