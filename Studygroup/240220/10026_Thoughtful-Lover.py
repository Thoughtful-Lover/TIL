'''
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

R : 빨강
G : 초록
B : 파랑

일반인 4개 구역으로 인식
적록색약 3개 구역으로 인식

첫째 줄 N (1 <= N <= 100)
둘째 줄부터 N개 줄에 그림이 주어진다.

일반인이 보는 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력
'''

import sys


def section(ii, jj):
    color = pic[ii][jj]
    pic[ii][jj] = -1

    for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
        ni = ii + di
        nj = jj + dj

        while 0 <= ni < N and 0 <= nj < N and pic[ii][jj] == color:
            if pic[ni][nj] == color:
                    pic[ni][nj] = -1
            else: break

    global count
    count += 1

    section(ni, nj)


N = int(sys.stdin.readline())
pic = [list(sys.stdin.readline()) for _ in range(N)]
count = 0

section(0, 0)

print(count)