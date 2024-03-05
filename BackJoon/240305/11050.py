'''
11050. 이항 계수 1

자연수 N과 정수 K가 주어졌을 때, 이항 계수 (N K) 뭐시기를 구해라

이항 계수 : 정확히 뭐에 쓰는지는 모르겠는데
(N K) = N!/ K! * (N-K)!

나중에 이항 계수 개념을 다시 찾아보자
'''


# 팩토리얼을 계산하는 함수를 정의
def factorial(num, times):
    while num > 1:
        times *= num
        num -= 1

    return times


N, K = map(int, input().split())

# 이항 계수를 구하는 공식에 따라 필요한 값들을 계산하고
N_fact = factorial(N, 1)
K_fact = factorial(K, 1)
N_K_fact = factorial(N-K, 1)

# 공식대로 계산해줌
print(N_fact // (K_fact*N_K_fact))