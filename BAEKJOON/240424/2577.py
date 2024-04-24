'''
2577. 숫자의 개수

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
'''

# 세 개의 정수를 입력 받고
A = int(input())
B = int(input())
C = int(input())
# 세 수를 곱한 값을 변수 numbers에 저장하고
numbers = A*B*C
# 이 값을 문자열로 만들어 각각의 숫자를 요소로 가지는 리스트를 만들어 준다.
numbers = list(str(numbers))
# numbers 속 숫자의 개수를 저장할 리스트 result를 정의해주고 0~9까지 인덱스 값으로 접근하기 위해 10개의 요소를 만들어 준다.
result = [0]*10

# numbers를 순회하며 numbers의 수를 int로 바꿔주고 result에서 해당 인덱스의 값을 1 증가시켜준다.
for char_num in numbers:
    num = int(char_num)
    result[num] += 1

# 완성된 result의 요소를 한 줄에 하나씩 출력해준다.
for cnt in result:
    print(cnt)