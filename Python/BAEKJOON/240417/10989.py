'''
10989. 수 정렬하기 3

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
'''

# 빠른 입력을 위해 sys를 import
import sys

# 이 수는 최대 10000이므로, 0~10000까지 인덱스를 가지는 배열 num_list를 선언
num_list = [0] * 10001
# N을 입력 받고
N = int(sys.stdin.readline())
# N개의 수만큼 num_list의 인덱스 번호에 해당하는 수를 증가시켜줌
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1

# 리스트를 순회하며
for i in range(10001):
    # 해당 인덱스에 있는 수만큼, 해당 인덱스를 출력해줌
    for _ in range(num_list[i]):
        print(i)