'''
1402. 아무래도이문제는A번난이도인것같다

어떤 정수 A가 있으면
A = a1 * a2 * a3 * a4, A' = a1 + a2 + a3 + a4 이면
A는 A'로 변할 수 있다.

A와 B가 주어지면 A는 B로 변할 수 있는지 판별

첫째 줄에는 테스트 케이스의 개수 T ( 1 <= T <= 100)
테스트 케이스마다 두 정수 A, B (-2^31 <= A, B <= 2^31 - 1 )
각각의 테스트 케이스마다 한 줄에 변할 수 있으면 yes, 아니면 no를 출력
'''

def add(array, target, current):
    fo



T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    # 먼저 B를 여러 정수의 덧셈 형태로 이리저리 조합해보고
    # 이 정수들의 곱이 A가 되는 경우가 있으면 yes를 출력
    B_list = [1]*B
    add(B_list, A, -1)
