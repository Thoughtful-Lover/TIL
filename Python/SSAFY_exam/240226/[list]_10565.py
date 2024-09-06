'''
10565 .
4828. 1일차 - min max (제출용)

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
'''


# 주어진 정수의 리스트 중 최대값과 최소값의 차이를 반환하는 함수 f
def f():
    # 최소값 min_sum 과 최대값 max_sum 에 초기값으로 리스트의 인덱스 0 값을 입력
    min_sum = arr[0]
    max_sum = arr[0]

    # 리스트를 순회하며 리스트 내의 값이 min_sum 보다 작거나 max_sum 보다 크면 바꿔줌
    for num in arr:
        if min_sum > num:
            min_sum = num
        if max_sum < num:
            max_sum = num
    return max_sum - min_sum


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {f()}')