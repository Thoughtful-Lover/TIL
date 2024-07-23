'''
1402. 아무래도이문제는A번난이도인것같다
A, B 에 대하여
A = a * b * c * ... * z , B = a + b + c + ... + z
A는 B로 변할 수 있다.

A와 B가 주어질 때, A는 B로 변할 수 있는지 판별하라

첫째 줄에 테스트 케이스의 개수 T (1 <= T <= 100)
테스트 케이스마다 두 정수 A, B ( -2^31 <= A, B <= 2^31-1)

각각의 테스트 케이스마다 한 줄에 변할 수 있으면 yesm 아니면 no를 출력
'''


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A > 0:
        if A >= B:
            print('no')
        elif A < B:
            print('yes')
    elif A < 0:
        if A > B:
            print('yes')
        elif A <= B:
            print('no')
    else:
        print('yes')