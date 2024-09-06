'''
활주로를 건설해보자

N*N 크기의 절벽지대에 활주로를 건설하려고 한다.
각 셀의 숫자는 지형의 높이
가로 또는 세로 방향으로 활주로를 건설할 수 있는 가능성

높이가 동등한 구간에서 가능
높이가 다른 구간에서는 높이가 1이고 길이가 x인 경사로를 설치하면 활주로로 사용할 수 있다.
활주로를 건설할 수 있는 경우의 수를 찾아보자

1. 6 ≤ N ≤ 20, N은 정수
2. 경사로의 높이는 항상 1, 길이 X는 정수, 2 <= X <= 4
3. 지형의 높이는 1 이상 6 이하의 정수
4. 동일한 셀에 두 개 이상의 경사로를 겹쳐서 사용할 수는 없다.
'''


def airstrip():
    global cnt

    for i in range(N):
        '''하나는 세로방향을 고정하고 가로방향을 탐색
        하나는 가로방향을 고정하고 세로방향을 탐색'''
        checkline(i, 0)
        checkline(0, i)


def checkline(y, x):
    sp = cliff[y][x]
    ground = 1
    for j in range(1, N):
        gap1 = cliff[i][j] - sp1
        gap2 = cliff[j][i] - sp2
        if gap1 == 0:
            ground1 += 1
        elif gap1 > 0:
            if gap1 == 1 and X <= ground1:
                sp1 = cliff[i][k]
                ground1 = 1
                continue
            break
        elif gap1 < 0:



        # 적힌 숫자가 차이가 (높이 차이) * X 만큼 있으면 극복 가능
        # 하나를 append 하고 같은 수가 나오면 계속 append 해
        # 다른게 나오면 가능한지 여부를 검사하고 가능하면 계속 진행해
        # 모두 성공하면 cnt += 1
        # 단 경사로는 지대가 낮은 경우에만 가능하지



T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(M)]
    cnt = 0

    airstrip()