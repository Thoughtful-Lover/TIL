'''
11659. 구간 합 구하기 4

수가 N개가 주어질 때 i번째 수부터 j번째 수까지 합을 구하는 프로그램

첫째 줄에 수의 개수 N 합을 구해야 하는 횟수 M
둘째 줄에 N개의 수
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j
'''


''' 시간초과
import sys

# N은 수의 개수, M은 주어지는 구간의 개수
N, M = map(int, sys.stdin.readline().split())
# N개의 수를 리스트 numbers에 할당
numbers = list(map(int, sys.stdin.readline().split()))
# M번 수행
for _ in range(M):
    # i번째부터 j번째까지의 구간합을 구할 예정
    i, j = map(int, sys.stdin.readline().split())
    # 구간의 합을 저장할 변수 num_sum
    num_sum = 0
    # i번째와 j번째 수의 인덱스는 i-1 ~ j-1
    for k in range(i-1, j):
        num_sum += numbers[k]
    # 구한 합을 출력
    print(num_sum)'''

import sys

# N은 수의 개수, M은 주어지는 구간의 개수
N, M = map(int, sys.stdin.readline().split())
# N개의 수를 리스트 numbers에 할당
numbers = list(map(int, sys.stdin.readline().split()))
for l in range(len(numbers)):
    if l > 0:
        numbers[l] += numbers[l-1]
# M번 수행
for _ in range(M):
    # i번째부터 j번째까지의 구간합을 구할 예정
    i, j = map(int, sys.stdin.readline().split())
    # 구한 합을 출력
    if i == 1:
        print(numbers[j-1])
    else:
        print(numbers[j-1]-numbers[i-2])