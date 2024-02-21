'''
9086. 문자열

문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램

입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
각 테스트 케이스는 한 줄에 하나의 문자열
알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.
'''


import sys

T = int(sys.stdin.readline())
for tc in range(T):
    # 문자열을 리스트로 입력 받음. readline 을 사용하니까 뒤에 줄바꿈 부호가 입력되어서 제거해줌
    my_str = list(sys.stdin.readline().rstrip())

    # 첫 번째 문자와 마지막 문자를 붙여서 출력
    print(my_str[0], end = '')
    print(my_str[-1])