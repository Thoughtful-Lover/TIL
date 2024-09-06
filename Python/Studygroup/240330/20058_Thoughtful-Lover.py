'''
20058. 마법사 상어와 파이어스톰

파이어볼과 토네이도를 조합해 파이어스톰
2^N * 2^N 인 격자판
(r, c)는 r행 c열
A[r][c]는 (r,c)에 있는 얼음의 양
값이 0이면 얼음이 없음

단게 L을 결정
2^L * 2^L 부분격자로 나눠 모두 90도 회전

이후 얼음이 있는 칸과 3칸 이상 인접해 있지 않은 칸은 얼음의 양이 1 줄어든다.

파이어스톰을 총 Q번 시전
1. 남아 있는 얼음의 합
2. 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
'''


def tornado(l):
    rotated_A = [[0]*(2**N) for _ in range(2**N)]
    sub_level = 2**l
    start_i = 0
    start_j = 0

    for i in range(sub_level):
        for j in range(sub_level):
            rotated_A[j][2**l-1-i] = A[i][j]
        for k


    pass


def fireball():
    # 테두리를 먼저 탐색하고
    # 중심부를 탐색
    pass


N, Q = map(int, input().split())
A = [list(input().split()) for _ in range(2**N)]
L = list(map(int, input().split()))

for level in L:
    tornado(level)