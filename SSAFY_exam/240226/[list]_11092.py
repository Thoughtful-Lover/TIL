'''
11092 .
최대 최소의 간격

N 개의 정수가 주어질 때,
1~N개의 위치값 중
가장 큰 수의 위치와, 가장 작은 수의 위치의 차이를 절대값으로 출력

단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
'''


# 최대인 값과 최소인 값의 위치의 차이의 절대값을 구하는 함수 f
def f():
    # 가장 큰 수와, 그 인덱스 값을 저장하는 max_num, 가장 작은 수와 그 인덱스 값을 저장하는 min_num
    max_num = [arr[0], 0]
    min_num = [arr[0], 0]

    '''
    리스트를 순회하며 max_num 보다 큰 값이나 min_num 보다 작은 값이 있으면 바꿔주고 인덱스 위치 정보도 바꿔준다.
    가장 작은 수가 여러 개이면 맨 먼저 나온 값을, 가장 큰 수가 여러 개이면 맨 마지막 값을 활용해야 하므로, 
    max_num 을 비교하는 조건문에는 둘 값이 같은 경우를 추가해주어 같은 값이면 마지막으로 나온 값으로 갱신해주도록 한다.
    '''
    for i in range(N):
        if max_num[0] <= arr[i]:
            max_num[0] = arr[i]
            max_num[1] = i
        if min_num[0] > arr[i]:
            min_num[0] = arr[i]
            min_num[1] = i

    # 문제에서 위치 정보는 1-N까지로 되어 있는데 위치 정보를 출력하는 것이 아니라 위치 정보의 차이를 출력하는 것이므로 인덱스 간의 차이를 구해주면 된다.
    result = max_num[1] - min_num[1]

    # 두 값의 위치 정보의 차이가 음수 일 때는 양수로 바꾸어 준다.
    if result < 0:
        return -result
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {f()}')
