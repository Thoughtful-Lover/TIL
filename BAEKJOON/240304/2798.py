'''
2798. 블랙잭

카드 개수 N
목표수 M
N개 카드 중 3개를 합할 때,
M을 넘지 않으면 M과 가장 가까운 수를 출력
'''


# 위의 방식에 맞는 새로운 블랙잭을 시행한다.
def new_blackjack(start, three_sum, cnt):
    global min_M

    # 카드를 3번 더하고 나면, 기존에 min_M에 저장된 값과 비교해 합이 이 값보다 크고 M보다 작거나 같으면 값을 갱신
    if cnt == 4:
        if min_M < three_sum <= M:
            min_M = three_sum
        return

    # 카드를 하나 선택하고 값을 더해주고 그 카드 이후에 있는 카드들 중 하나를 선택하여 더해보고 하는 과정을 진행1
    for i in range(start, N):
        new_blackjack(i+1, three_sum+cards[i], cnt+1)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
# M을 넘지 않으면 M과 가장 가까운 수를 저장할 변수 min_M을 정의
min_M = 0
new_blackjack(0, 0, 1)

print(min_M)