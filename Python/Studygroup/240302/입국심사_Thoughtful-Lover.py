'''
M명의 입국 심사
심사대 N개
각각 걸리는 시간

입국 심사를 마치는데 걸리는 최소 시간은?

T : 테스트 케이스 수
N, M: 1 ≤ N ≤ 10^5, 1 ≤ M ≤ 10^9
다음 N개의 줄의 k번째 줄에는 tk (1 ≤ tk ≤ 10^9)가 주어진다.
'''


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    checkpoint = [0] * N
    for i in range(N):
        tk = int(input())
        checkpoint[i] = tk
    checktime = checkpoint[:]

    while M > 0:
        mv = min(checktime)
        mi = checktime.index(mv)
        checktime[mi] += checkpoint[mi]
        M -= 1

    print(f'#{tc} {mv}')