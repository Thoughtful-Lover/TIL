'''
4101. 크냐?

두 양의 정수가 주어졌을 때,
첫 번째 수가 두 번째 수보다 크면 Yes를, 아니면 No
'''


while True:
    try:
        A, B = map(int, (input().split()))

        # 왼쪽이 오른쪽보다 크면 Yes 출력
        if A - B > 0:
            print('Yes')

        elif A == B == 0:
            pass

        # 나머지 경우는 No 출력
        else: print('No')

    except:
        break