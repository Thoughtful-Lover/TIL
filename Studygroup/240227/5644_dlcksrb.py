'''
스마트폰을 무선 충전할 때 최적의 BC (Battery Charger)를 선택하는 알고리즘

일정 거리 안에 왔을 때 충전이 가능
단, 같은 충전을 여럿이 쓸 경우 충전량을 나눠 가진다
최대로 얻을 수 있는 충전량은?

1. 지도의 가로, 세로 크기는 10이다.
2. 사용자는 총 2명이며, 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발한다.
3. 총 이동 시간 M은 20이상 100이하의 정수이다. (20 ≤ M ≤ 100)
4. BC의 개수 A는 1이상 8이하의 정수이다. (1 ≤ A ≤ 8)
5. BC의 충전 범위 C는 1이상 4이하의 정수이다. (1 ≤ C ≤ 4)
6. BC의 성능 P는 10이상 500이하의 짝수이다. (10 ≤ P ≤ 500)
7. 사용자의 초기 위치(0초)부터 충전을 할 수 있다.
8. 같은 위치에 2개 이상의 BC가 설치된 경우는 없다. 그러나 사용자A, B가 동시에 같은 위치로 이동할 수는 있다.
사용자가 지도 밖으로 이동하는 경우는 없다.

T: 테스트 케이스 수
M, A: 총 이동 시간, BC의 개수
'''


def f():
    # 이동의 경우의 수
    move = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

    # 사용자 A와 B의 초기 위치는
    Ai, Aj = 1, 1
    Bi, Bj = 10, 10

    charing(Ai, Aj, Bi, Bj)

    for i in range(M):
        Ai += move[uA[i]][0]
        Aj += move[uA[i]][1]
        Bi += move[uB[i]][0]
        Bj += move[uB[i]][0]

        charging(Ai, Aj, Bi, Bj)


def charging(ai, aj, bi, bj):
    global quant

    q1 = []
    q2 = []

    for j in range(A):
        if abs(BC[j][0]-ai)+abs(BC[j][1]-aj) <= BC[j][2]:
            q1.append(BC[j][3])
        if abs(BC[j][0]-bi)+abs(BC[j][1]-bj) <= BC[j][2]:
            q2.append(BC[j][3])

    if q1 and q2:
        q1.sort()
        q2.sort()
        quant += q1[-1]
        if q1[-1] == q2[-1]:
            if q1[-2] > q2[-2]:     # 여기다가 2개 이상 없는 경우도 넣어놔야 하는거잖아 !!!
                quant += q1[-2]
            else:
                quant += q2[-1]
        else:
            quant += q2[-1]

    elif q1:
        mA = max(q1)
        quant += mA
    elif q2:
        mB = max(q2)
        quant += mB

# 각각의 출발점에서 매번 움직이며 움직일 때마다 BC 와의 거리를 계산
# 충전 범위에 있으면 충전을 진행
# 단 충전 범위가 겹치는 경우 겹치지 않게 제약 조건


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    uA = list(map(int, input().split()))
    uB = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]
    # 사용자 A와 B의 충전량을 모두 저장
    quant = 0

    print(f'#{tc} {f()}')
