def swimming_pool(d, m, q, y):
    # 테스트 케이스를 보니 꼭 긴 기간의 사용권이 가장 저렴한 건 아니더라
    # 그렇다면 기간대비 가장 저렴한 사용권을 가장 적게 사용하는 방법을 생각해봐야지
    qm = q/3
    ym = y/12
    cnt = 0
    for i in range(12):
        sub_fee = 0
        if plan[i] == 0:
            continue
        sub_fee = plan[i] * d
        if sub_fee > m:
            sub_fee = m
        if sub_fee > ym:
            cnt += 1
            continue






T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))
    fee = [0] * 12

    print(f'#{tc} {swimming_pool(day, month, quarter, year)}'
