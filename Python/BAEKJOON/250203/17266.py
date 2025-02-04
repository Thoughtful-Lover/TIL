# 굴다리의 길이 N, 가로등의 개수 M, 가로등의 위치 정보 lights
N = int(input())
M = int(input())
lights = list(map(int, input().split()))

# 가로등이 비취어야 하는 거리 정보를 저장할 배열 distance
distance = list()

# 초기 값으로 굴다리의 처음과 첫 가로등과의 거리, 굴다리의 끝과 마지막 가로등과의 거리를 저장
distance.append(lights[0])
distance.append(N-lights[-1])

# 가로등 전체를 순회하며
for i in range(1, M):
    # 가로등과 가로등 사이의 거리를 계산하고
    v = lights[i]-lights[i-1]
    # 가로등의 높이가 무조건 정수여야 하므로, 홀수이면 한 치수 크게 거리를 계산해주고
    if v%2:
        distance.append(v//2+1)
    # 짝수인 경우 그냥 절반만큼 거리를 계산해주면 됨
    else:
        distance.append(v//2)
print(max(distance))