'''
10826. 피보나치 수 4

피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
Fn = Fn-1 + Fn-2 (n ≥ 2)
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
첫째 줄에 n이 주어진다. n은 10,000보다 작거나 같은 자연수 또는 0이다.
'''

# 이전 값을 변수 prev, 현재 값을 변수 now, 변수 current 에는 현재 몇 번째 수인지를 저장
prev = 0
now = 1
current = 1

# 목표 값인 n번째 수를 입력 받음
n = int(input())

# current 값이 n에 도달하지 않을 동안
while n > current:
    # next 에 이전 값 2개를 더한 값을 더해주고
    next = prev + now
    # now 값과 next 값을 한 칸씩 뒤로 밀고
    prev = now
    now = next
    # current 값을 1 증가
    current += 1

# 종료 조건은 current = n 일 때, 현재값 now를 출력
# 단, n=0이면, now가 아닌 prev인 0 값을 출력 (이전 문제들과의 차별점)
if n == 0:
    print(0)
else:
    print(now)