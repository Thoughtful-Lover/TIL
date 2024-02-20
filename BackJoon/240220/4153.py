'''
주어진 3개의 정수
세 변의 길이로 삼각형이 직각인지 아닌지를 구분
'''


while True:
    # 리스트로 입력 받음
    arr = list(map(int, input().split()))

    # 만약 0 0 0 이 입력되면 반복문을 종료
    if arr[0] == arr[1] == arr[2] == 0:
        break

    # 피타고라스 정리에 의해 빗변의 제곱이, 나머지 2개의 제곱의 합과 같으면 직각삼각형
    # 계산을 편리하게 하기 위해 피타고라스 정리의 양변에 빗변의 제곱을 더한 값을 조건으로
    elif arr[0]**2 + arr[1]**2 + arr[2]**2 == 2*max(arr)**2:
        print('right')
    else:
        print('wrong')

