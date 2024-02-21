'''
270. 수 정렬하기

문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

def sort_numb(num_list):
    num_list.sort()

    # 리스트의 원소를 한 줄에 하나씩 출력
    for number in num_list:
        print(number)


N = int(input())
arr = [0] * N
# 한 줄에 하나씩 입력 받아 리스트에 저장
for i in range(N):
    num = int(input())
    arr[i] = num

sort_numb(arr)