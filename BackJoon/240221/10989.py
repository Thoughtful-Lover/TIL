'''
10989. 수 정렬하기 3

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)
둘째 줄부터 N개의 줄에는 수 (10,00보다 작거나 같은 자연수)
오름차순으로 정렬
'''


def sort_numb(num_list):
    num_list.sort()
    '''
    # 메모리 초과
    for j in range(N - 1):
        for k in range(1, N):
            if num_list[j] > num_list[k]:
                num_list[j], num_list[k] = num_list[k], num_list[j]
                '''
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

