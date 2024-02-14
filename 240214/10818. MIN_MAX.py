'''
N개의 정수
최솟값과 최대값 출력
'''


min = 1000000       # min 을 가능한 최대값으로 설정
max = -1000000      # max 를 가능한 최소값으로 설정

N = int(input())
arr = list(map(int, input().split()))       # 입력값을 리스트로 받아서

for i in arr:       # 리스트를 순회하며
    if i < min:     # 리스트의 원소가 min 보다 작으면 대체
        min = i
    if i > max:     # 리스트의 원소가 max 보다 크면 대체
        max = i

print(min, max)