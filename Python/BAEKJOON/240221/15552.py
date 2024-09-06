'''
15552. 빠른 A+B
'''


# 시간을 줄이기 위해 sys 를 import
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)