'''
20053. 최소, 최대 2

N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

# 테스트 케이스 수를 입력 받고
T = int(input())
# 각 테스트 케이스 별 시행
for _ in range(T):
    # 정수의 개수 N
    N = int(input())
    # 정수의 배열을 입력 받고
    numbers = list(map(int, input().split()))
    # 최소, 최대값을 각각 출력
    print(min(numbers), max(numbers))