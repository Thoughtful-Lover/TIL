'''
2738. 행렬 덧셈

문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다.
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다.
행렬의 각 원소는 공백으로 구분한다.
'''

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):  # 입력 받은 행렬의 리스트 A에 B의 값을 더함
    for j in range(M):
        A[i][j] += B[i][j]

for i in range(N):  # 조건에 맞게 각 행별로 출력
    print(*A[i])

# 행렬에서 N과 M이 무엇을 의미하는지 잘 생각해보기
