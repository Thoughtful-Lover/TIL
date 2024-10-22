import re

N = int(input())
M = int(input())
S = input()
# N+1개의 I와 N개의 O로 이루어진 수 N
PN = 'IO'*N+'I'

print(re.findall(PN, S))