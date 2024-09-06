'''
[SW Test 샘플문제] 프로세서 연결하기

N * N 크기의 cell
1개의 cell 에는 1 개의 Core 또는 전선
가장 자리에는 전원

Core와 전원을 연결하는 전선으로 직선으로만 설치
전선은 교차하면 안됨

최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합
=> 그러면 꼭 모든 core 를 연결할 필요는 없나?

여러 방법이 있을 때는 전선 길이의 합이 최소가 되는 경우

1. 7 ≤  N ≤ 12
2. Core의 개수는 최소 1개 이상 12개 이하이다.
3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.
'''

T = int(input())
for tc in range(T, T+1):
    pro = [list(map(int, input().split())) for _ in range(N)]

    for 1 in pro: