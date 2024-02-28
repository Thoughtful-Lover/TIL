'''
1486 .
장훈이의 높은 선반

점원들의 키를 합친 탑의 높이가 선반보다 이상인 탑 중에서 가장 낮은 탑을 알아내려고 한다.

T : 테스트 케이스 수
N, B : 직원의 수 N, 선반의 높이 B
직원들 키의 배열
'''

'''
1
5 16
1 3 3 5 6

내가 만든 테케
1
8 12
1 2 2 3 4 5 8 9
'''


# 재귀로 해야지
def human_tower(n):
    global height_sum

    if arr[n] > M:
        human_tower(-1)
    if n != -1 and height_sum == 0:
        height_sum += arr[n+1]
        return
    height_sum += arr[n]
    if height_sum >= M:
        return height_sum-M


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    height_sum = 0

    human_tower(-1)

    print(f'#{tc} {human_sum-M}')
