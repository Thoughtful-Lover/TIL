'''
5355. 화성 수학

화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다.
입력으로 주어지는 수는 정수이거나 소수 첫째 자리까지 주어지며, 0 이상 100 이하이다.
연산자는 최대 3개 주어진다.

각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.
'''


# 화성에서의 연산자를 통해 연산을 수행하는 함수 mars_calculate를 정의
# 리스트인 array를 입력 받음
def mars_calculate(array):
    # 입력으로 주어지는 수가 정수이거나 소수 첫째 자리까지 주어지므로 문자열로 입력받은 리스트를 float()로 실수형으로 변환해준다.
    num = float(array[0])
    # 리스트의 길이를 변수 length에 저장해주고
    length = len(array)
    # 주어진 수 이후의 연산자를 순회하며
    for i in range(1, length):
        # @ 이면 3을 곱해주고
        if array[i] == '@':
            num *= 3
        # % 이면 5를 더해주고
        elif array[i] == '%':
            num += 5
        # # 이면 7을 빼준다.
        elif array[i] == '#':
            num -= 7
    # 결과값을 반환
    return num


# 테스트케이스의 수 T를 입력 받음
T = int(input())
# 테스트 케이스별 시행
for _ in range(T):
    # 수식의 내용을 문자열 리스트로 입력 받고
    math_equation = list(input().split())
    # 이 리스트를 함수에 입력하고 그 결과를 변수 result에 저장
    result = mars_calculate(math_equation)
    # 출력 조건에 맞게 소수점 둘째자리까지 출력
    print(f'{result:.2f}')