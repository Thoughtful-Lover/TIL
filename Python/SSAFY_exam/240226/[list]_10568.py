'''
10568 .
4834. 1일차 - 숫자 카드 (제출용)

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''


def f():
    global max_card_num
    global max_card

    # string 으로 입력 받은 카드의 리스트를 int로 바꾸어 해당 인덱스에 해당하는 check 의 값을 1씩 증가
    for num in arr:
        check[int(num)] += 1

    # check 리스트를 순회하며 해당 값에 저장된 값이 max_card_num 보다 크거나 같으면 max_card_num 과 max_card 를 갱신
    for i in range(10):
        if max_card_num <= check[i]:
            max_card_num = check[i]
            max_card = i


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    # 카드의 개수를 세어줄 check 를 정의
    check = [0] * 10

    # 가장 많은 카드의 개수 max_card_num, 가장 많은 카드의 번호 max_num
    max_card_num = 0
    max_card = 0

    # 함수를 호출
    f()

    print(f'#{tc} {max_card} {max_card_num}')