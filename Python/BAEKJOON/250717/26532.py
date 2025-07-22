# 각각의 값을 입력 받음
a, b = map(int, input().split())
# 직사각형의 면적인 size
size = a*b
# 옥수수 가방 하나가 덮을 수 있는 면적을 야드 단위로 계산
corns = 4840*5
# 가방의 개수는 직사각형의 면적을 커버가능한 면적으로 나눈 것
bags = size//corns
# 이때 해당 값에 난머지가 있으면 가방 개수 1 추가
if size%corns:
    bags += 1
print(bags)