'''
10989. 수 정렬하기 3

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
'''


N = int(input())
# 리스트에 숫자를 하나씩 입력해 넣고
num_list = [0] * N
for i in range(N):
    num_list[i] = int(input())

# 숫자 리스트를 정렬해서
num_list.sort()
# 하나씩 출력
for num in num_list:
    print(num)
