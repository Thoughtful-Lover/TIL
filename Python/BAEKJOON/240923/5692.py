'''
5692. 팩토리얼 진법

어떤 수가 주어졌을 때 오른쪽 부터 1!, 2!, 3!, ..., n! 의 자리수라고 한다.
해당 수가 주어졌을 때 하당 수의 십진법 값을 구하시오
입력의 마지막 줄에 영이 하나 입력
'''

''' # 1차 시도_시간 초과
# 해당 팩토리얼 진수를 계산하는 함수 factorialNumber를 정의
# 매개변수로 구하려는 팩토리얼 진수의 길이와, 팩토리얼 진수의 값을 리스트로 받을 예정
def factorialNumber(n:int, number: list):
    # 해당수를 10진수로 변환한 결과값을 저장할 변수 answer
    answer = 0
    # 해당수를 1!의 자리수부터 계산해주려고 함
    for i in range(1, n+1):
        # 해당 자리수에 해당하는 수를 하나 꺼내고
        num = int(number[-i])
        # 그 수에 해당하는 팩토리얼 값을 곱해줌
        for j in range(1, i+1):
            num *= j
        # 해당 값을 answer에 저장
        answer += num
    # 위 반복문을 마치고 저장된 answer 값을 반환
    return answer

while True:
    # 입력 받을 수를 list 형태로 입력 받고
    numberArray = list(input())
    # 종료 조건인 0 값이 나오면 반복문을 종료
    if numberArray[0] == '0':
        break
    # 그게 아니면 함수의 결과값을 출력
    print(factorialNumber(len(numberArray), numberArray))
'''

''' # 2차 시도_시간 초과
# 문제에서 길이가 최대 5라고 했으니까 그냥 해당하는 값을 하드 코딩해서 풀어보자
factorial_number = [120, 24, 6, 2, 1]

while True:
    number = list(input())
    if number[0] == '0':
        break
    cnt = 0
    for i in range(1, len(number)+1):
        cnt += int(number[-i])*factorial_number[-i]
    print(cnt)
'''

# 3차 시도_성공
# 이거 입력 방법을 바꿔야되는 거였네
import sys


# 해당 팩토리얼 진수를 계산하는 함수 factorialNumber를 정의
# 매개변수로 구하려는 팩토리얼 진수의 길이와, 팩토리얼 진수의 값을 리스트로 받을 예정
def factorialNumber(n:int, number: list):
    # 해당수를 10진수로 변환한 결과값을 저장할 변수 answer
    answer = 0
    # 해당수를 1!의 자리수부터 계산해주려고 함
    # 이거 readline() 하면 마지막 값이 '\n'이 되므로 걸러야 됨
    for i in range(2, n+1):
        # 해당 자리수에 해당하는 수를 하나 꺼내고
        num = int(number[-i])
        # 그 수에 해당하는 팩토리얼 값을 곱해줌
        for j in range(1, i):
            num *= j
        # 해당 값을 answer에 저장
        answer += num
    # 위 반복문을 마치고 저장된 answer 값을 반환
    return answer

while True:
    # 입력 받을 수를 list 형태로 입력 받고
    numberArray = list(sys.stdin.readline())
    # 종료 조건인 0 값이 나오면 반복문을 종료
    if numberArray[0] == '0':
        break
    # 그게 아니면 함수의 결과값을 출력
    print(factorialNumber(len(numberArray), numberArray))