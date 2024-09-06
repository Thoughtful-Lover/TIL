'''
10567 .
4835. 1일차 - 구간합 (제출용)

N개의 정수가 들어있는 배열에서 이웃한 M개의 합
M개의 합 중 가장 큰 합과 가장 작은 합의 차이를 출력하는 프로그램
'''


def f(n, m):
    # 1 ≤ a ≤ 10000 이므로 구간합은 최대 10000*n을 넘을 수 없고, 최소한, n보다 크다
    min_sum = 10000*n
    max_sum = 1

    # 구간합의 시작점은 맨 처음부터, 구간합의 마지막 인덱스가 끝일 때까지
    for i in range(n-m+1):
        sum_t = 0
        # 이때 구간합의 길이만큼 합을 구해서
        for j in range(m):
            sum_t += arr[i+j]

        # 비교해줘서 최소합보다 작거나, 최대합보다 큰 값이 있으면 바꿔준다.
        if max_sum < sum_t:
            max_sum = sum_t
        if min_sum > sum_t:
            min_sum = sum_t

    # 최대 - 최소 를 반환
    return max_sum - min_sum


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{tc} {f(N, M)}')