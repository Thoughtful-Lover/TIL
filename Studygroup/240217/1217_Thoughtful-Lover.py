'''
class SWEA
1217. 거듭 제곱

N과 M이 주어질 때, N의 M 거듭제곱 값을
재귀 호출을 이용하여 구현해 보아라
'''


def power(n, m):
    global result

    if m == 0:
        return

    result *= n
    power(n, m-1)


for i in range(10):
    tc = int(input())
    N, M = map(int, (input().split()))
    result = 1  # 출력값을 저장해줄 result 정의

    power(N, M)

    print(f'#{tc} {result}')