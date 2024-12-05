# 조사한 시간 n과, 조사를 시작할 때 터널 안에 들어있는 차량의 수 m을 입력 받음
n = int(input())
m = int(input())
# 현재까지 터널 안에 있는 가장 많은 차량 대수를 저장할 변수 cars
cars = 0
# n분만큼 탐색
for _ in range(n):
    # 들어온 차량과 나온 차량의 값을 각각 입력 받음
    enter, out = map(int, input().split())
    # 기존에 터널에 있던 차량 대수에 들어가고 나간 차량 대수를 더함
    m += (enter-out)
    # 만약 현재 갱신된 터널 안 차량 대수가 0보다 적으면 그냥 값을 0으로 출력
    if m < 0:
        cars = 0
        break
    # 아니면 차량대수 값이 현재 값보다 적으면 값을 갱신
    elif cars < m:
        cars = m
# 반복을 마치면 저장된 값을 출력
print(cars)