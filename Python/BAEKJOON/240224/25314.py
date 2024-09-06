'''
25314. 코딩은 체육과목 입니다
'''

# 처리 시간을 줄이기 위해 sys import
import sys

# 4 <= N <= 1,000; N은 4의 배수
N = int(sys.stdin.readline())

# 조건에 따라 N=4*x, x 만큼 'long'을 출력해주고
for i in range(N//4):
    print('long', end = ' ')

# 마지막에 'int'를 출력
print('int')
