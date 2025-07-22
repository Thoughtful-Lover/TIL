# 리스트를 deque로만 바꾼 코드
from collections import deque

while True:
    # 암호를 문자열의 배열 형태로 입력
    password = deque(input())
    print(password)
    # 만약 입력 받은 문구가 END이면 종료
    if password == deque(['E', 'N', 'D']):
        break
    # 입력받은 암호를 뒤에서부터 하나씩 꺼내서 출력해줌
    while password:
        print(password.pop(), end='')
    # 바로 위의 반복이 끝났을 때 줄을 바꿔줌
    print()