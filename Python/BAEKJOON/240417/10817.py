'''
10817. 세 수
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
'''

# 세 수를 리스트로 입력 받고
nums = list(map(int, input().split()))
# 정렬한 후
nums.sort()
# 두 번째 인덱스 값을 출력한다.
print(nums[1])