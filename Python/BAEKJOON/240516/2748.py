'''
2748. 피보나치 수 2

n을 입력 받아
n번째 피보나치 수를 구하는 프로그램을 작성하시오.
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
print(now)