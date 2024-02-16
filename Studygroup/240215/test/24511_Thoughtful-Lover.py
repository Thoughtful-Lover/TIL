import sys
import copy
from collections import deque

N = int(sys.stdin.readline())
A = deque(map(int, sys.stdin.readline().split()))
B = deque(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = deque(map(int, sys.stdin.readline().split()))

# 출력할 값을 담을 return_list 를 정의
return_list = [0]*M

# C에 입력 받은 수열을 차례대로 자료 구조에 삽입
for i in range(M):
    ip = C[i]      # 삽입할 원소
    for j in range(N):
        if A[j] == 0:   # 자료 구조가 0 (큐 이면)
            # 기존에 들어가 있던 원소가 나오고, 자료 구조가 1이면 들어갔던 원소가 그대로 나옴
            B[j], ip = ip, B[j]
    return_list[i] = ip      # 마지막 자료구조까지 거쳐서 나온 값을 return_list 에 배정

# 출력 양식에 맞게 한 칸씩 띄워서 출력
print(*return_list)