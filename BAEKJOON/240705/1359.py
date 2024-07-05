'''
1359. 복권

1부터 N까지의 수 중에 서로 다른 M개의 수를 골라보세요.
저희도 1부터 N까지의 수 중에 서로 다른 M개의 수를 고를건데,
적어도 K개의 수가 같으면 당첨입니다.
'''


import math


# (안녕))/(전체에서 M개의 수를 뽑을 경우)
N, M, K = map(int, input().split())
print((math.factorial(M)/(math.factorial(K)*math.factorial(M-K)))*(math.factorial(N-K)/(math.factorial(N-M)*math.factorial(M-K)))/(math.factorial(N)/(math.factorial(M)*math.factorial(N-M))))