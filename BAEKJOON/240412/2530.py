'''
2530. 인공지능 시계

첫째 줄에는 현재 시각이 나온다.
현재 시각은 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.

종료되는 시각의 시, 분, 초를 공백을 사이에 두고 출력
'''

# A, B, C는 각각 현재 시간, 분, 초이고
# D는 걸리는 시간이다.
A, B, C = map(int, input().split())
D = int(input())

# 초에 D를 더해주고
C += D
# C에서 60이 넘어 분으로 전환되는 시간은 B에 더해주고
B += C//60
# C에는 남은 초를 저장한다.
C = C%60

# 마찬가지로 B에서 60분이 넘어 시로 전환되는 시간은 A에 더해주고
A += B//60
# B에는 남은 분을 저장한다.
B = B%60

# 마지막으로 혹시 A가 24시가 넘었을 경우 0시부터 시작되므로 이 부분을 처리해준다.
A %= 24

# 출력 양식에 맞게 출력한다.
print(f'{A} {B} {C}')