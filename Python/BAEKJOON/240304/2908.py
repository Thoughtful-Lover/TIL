'''
2908. 상수

세자리 수를 2개 입력 받으면
두자리를 거꾸로 읽고 둘 중에 큰 수를 출력
'''


# 백의 자리는 일의 자리로, 일의 자리는 백의 자리로, 십의 자리는 그대로 남기는 함수 reverse_num 을 정의
def reverse_num(number):
    number = (number % 10)*100 + ((number//10) % 10)*10 + number//100

    return number


A, B = map(int, input().split())

# 함수를 호출하여 역순으로 바꾼 수를 기존 변수명에 저장
A = reverse_num(A)
B = reverse_num(B)

# 바뀐 A가 바뀐 B보다 크면 A를 출력하고 아니면 B를 출력
if A > B:
    print(A)
else:
    print(B)