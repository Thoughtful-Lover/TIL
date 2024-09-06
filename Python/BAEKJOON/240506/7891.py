'''
7891. Can you add this?

Given two integers, calculate and output their sum.
'''


T = int(input())
# 테스트 케이스별 시행
for _ in range(T):
    # 2개의 integer를 입력 받고
    A, B = map(int, input().split())
    # 두 값의 합을 출력
    print(A+B)