'''
6679. 싱기한 네자리

[1000,9999]인 10진수 숫자중에서
숫자를 10진수, 12진수, 16진수로 나타낸 다음, 각각의 숫자에 대해, 각 숫자의 자리수를 더했을 때, 세 값이 모두 같아야 한다.

'''

a = 2999
a = hex(a)
print(a)
print(int('b', 16))

# sensing_info.to_middle => 차가 도로 중앙으로부터 멀어져 있는 거리
# self.half_road_limit => 도로의 중간 넓이 + 차체의 절반 넓이
# 차체의 절반 넓이 = 1m
while sensing_info.to_middle > self.half_road_limit-1:
    # 핸들을 왼쪽으로 꺾어
    car_controls.throttle = 0.5
    car_controls.steering = -0.7
# 뭔가 반복문 돌고 나면 핸들을 원상복구하고 차체를 원상복구 해줘야할 것 같은디
# 근데 형이 짜둔거 다음에 핸들 조정하는거 있으니까 어떻게든 되지 않을까? ㅋㅋㅋㅋ
while sensing_info.to_middle < self.half_road_limit-1:
    # 핸들을 오른쪽으로 꺾어
    car_controls.throttle = 0.5
    car_controls.steering = 0.7

# 도로 위에 있으면
# 앞의 도로의 꺾어지는 각도에 맞춰서 각도를 조정

self.half_road_limit
sensing_info.moving_angle