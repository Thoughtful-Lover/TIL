'''
23808. 골뱅이 찍기 - ㅂ

ㅂ자 모양은 가로 및 세로로 각각 5개의 셀로 구성되어 있다.
상자에는 정사각형 모양의 셀의 크기를 나타내는 숫자 하나가 적혀있다.
셀의 크기 N이 주어지면 예제 출력과 같은 방식으로 골뱅이 모양을 출력하시오.

if N == 1,
@   @
@   @
@@@@@
@   @
@@@@@

if N==3,
@@@         @@@
@@@         @@@
@@@         @@@
@@@         @@@
@@@         @@@
@@@         @@@
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
@@@         @@@
@@@         @@@
@@@         @@@
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
'''


# N = 1일 때, 기준으로 보면
'''
골빈빈빈골
골빈빈빈골
골골골골골
골빈빈빈골
골골골골골
'''
# 위와 같은 규칙이 있음을 알 수 있다.
# N = 3일 때와 비교해보면, 골이나 빈 하나의 값에 N*N개가 들어가는 것을 알 수 있다.
# 이 때, 모양이 같은 첫째, 둘째, 다섯째 줄을 empty 함수로, 셋째, 냈재 줄을 full 함수로 묶어준다.
def empty(num):
    for _ in range(num):
        print('@', end='')
    for _ in range(num):
        print(' ', end='')
        print(' ', end='')
        print(' ', end='')
    for _ in range(num):
        print('@', end='')
    print()


def full(num):
    for _ in range(num*5):
        print('@', end='')
    print()


N = int(input())
for _ in range(N*2):
    empty(N)
for _ in range(N):
    full(N)
for _ in range(N):
    empty(N)
for _ in range(N):
    full(N)