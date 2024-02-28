'''
2480. 주사위 세개
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
'''


# 주사위 눈에 따라 계산의 결과값을 출력하는 함수 three_dices
def three_dices(info):
    # 3개의 눈이 모두 같은 경우
    if info[0] == info[1] == info[2]:
        print(10000+info[0]*1000)
    # 3개의 눈이 모두 다른 경우
    elif info[0] != info[1] != info[2] and info[0] != info[2]:
        print(max(info) * 100)
    # 2개의 눈이 같은 경우
    else:
        # 같은 눈이 2번째, 3번째인 경우
        if info[1] == info[2]:
            print(1000+info[1]*100)
        # 나머지 경우
        else:
            print(1000 + info[0]*100)


dices = list(map(int, input().split()))
three_dices(dices)