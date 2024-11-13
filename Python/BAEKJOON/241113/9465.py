# 테스트 케이스 수 입력
T = int(input())
# 테스트 케이스 별 시행
for _ in range(T):
    # 열의 개수 N을 입력 받고
    N = int(input())
    # dp 배열을 만들어 버림
    dp = [[0] * N for _ in range(2)]

    # 스티커 정보를 입력 받음
    stickers = [[], []]
    for i in range(2):
        stickers[i] = list(map(int, input().split()))

    # dp 배열에 제일 첫번째 열의 값들과 두 번째 열의 값들을 저장해주고
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if N > 1:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

    # 반복 순회 하되 먼저, 현재 인덱스의 대각선에 위치한 값들을 입력
    # 해당 값의 dp 값과 현재 위치 dp 값과 대각선 위치의 스티커 값을 더한 값 중 더 큰 값을 저장
    # 다음으로 현재 위치에서 대각선 바로 오른쪽 값을 입력
    # 기존 dp 값과 현재 위치의 dp 값과 해당 위치의 스티커 값을 덧한 값 중 더 큰 값을 저장
    for j in range(2, N):
        dp[0][j] = max(dp[1][j - 2], dp[1][j - 1]) + stickers[0][j]
        dp[1][j] = max(dp[0][j - 2], dp[0][j - 1]) + stickers[1][j]
    # 위의 반복을 마친 후 마지막 열의 dp 값 중 더 큰 값을 출력
    print(max(dp[0][N - 1], dp[1][N - 1]))