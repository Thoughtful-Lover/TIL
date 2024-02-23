'''
2480. 주사위 세개
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
'''


def three_dices(info):
    if info[0] == info[1] == info[2]:
        print(10000+info[0]*1000)
    elif info[0] != info[1] != info[2] and info[0] != info[2]:
        print(max(info) * 100)
    else:
        print(1000+)


dices = list(map(int, input().split()))
three_dices(dices)