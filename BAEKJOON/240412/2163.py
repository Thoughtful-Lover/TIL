'''
2163. 초콜릿 자르기

N*M 크기의 초콜릿을
N*M 개의 조각으로 나눈다.

적당한 위치에서 초콜릿을 조개고 이 중 하나의 초콜릿 조각을 들고 쪼개는 과정을 반복

첫째 줄에 두 정수 N, M (1 <= N, M <= 300)
'''


# N과 M을 입력 받음
N, M = map(int, input().split())
# 초콜릿을 한 번 쪼갤 때마다 초콜릿 조각은 +1개가 됨
# 1개에서 2개로 만들 때 한번, 2개에서 3개로 만들 때 한번
# 이런 식으로 생각해보면 N*M개의 조각을 만드려면 N*M-1 번 쪼개면 된다는 것을 알 수 있다.
print(N*M-1)