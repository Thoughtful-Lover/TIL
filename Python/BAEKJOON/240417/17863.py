'''
17863. FYI

미국의 전화번호는 7개 숫자로 이루어져 있다.
시작하는 첫 수(prefix number)가 '555'이면 YES를, 아니면 NO를 출력하라
'''


# prefix number를 확인하는 함수 fyi를 정의
def fyi(phone_number):
    for i in range(3):
        # 앞의 세 번호 중 하나라도 5가 아니면 NO를 출력
        if phone_number[i] != '5':
            print('NO')
            return
    # 모두 5라면 YES를 출력
    print('YES')
    return


# 주어진 전화번호를 문자열 리스트로 입력받고
phone_numbers = list(input())
# 함수에 매개변수로 넣는다
fyi(phone_numbers)