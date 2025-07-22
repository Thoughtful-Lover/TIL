# 해당하는 수가 1~10 사이의 자연수이므로 초기 시작점과 끝점으로 1과 10을 설정
sp, ep = 1, 10
# 스탠이 하는 말의 진위 여부를 저장할 변수 TF, 초기값은 True
TF = True
# 반복문
while True:
    # 올리가 외친 수 num
    num = int(input())
    # 만약 수가 0이라면, 반복 종료
    if not num:
        break
    # 스탠의 대답 answer
    answer = input()
    # 만약 too high라고 했는데
    if answer == 'too high':
        # 외친 수가 기존에 저장된 구간의 시작점보다 작거나 같으면
        if num<=sp:
            # 거짓말
            TF = False
        # 그게 아니라면 구간의 종료지점을 갱신
        elif num<ep:
            ep = num
    # 마찬가지로 too low라고 외쳤을 때
    if answer == 'too low':
        # 구간의 종료지점보다 외친 값이 크거나 같다면, 거짓말
        if num>=ep:
            TF = False
        # 그게 아니라면, 시작 지점을 갱신
        elif num>sp:
            sp = num
    # 만약 right on이라고 한다면
    if answer == 'right on':
        # 외친 수가 기존의 구간에 포함 되어 있지 않다면, 거짓말
        if not sp<=num<=ep:
            TF = False
        # 그리고 기존에 저장된 정보를 확인하여 사실, 거짓 여부를 출력하고
        if TF:
            print('Stan may be honest')
        elif not TF:
            print('Stan is dishonest')
        # 구간 정보와 진위 여부를 초기화
        sp, ep = 1, 10
        TF = True