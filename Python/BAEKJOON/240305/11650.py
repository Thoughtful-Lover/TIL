'''
11650. 좌표 정렬하기

2차원 평면 위의 점 N개
좌표를 x에 대해 x 좌표가 증가하는 순
x 좌표가 같으면 y 좌표가 증가하는 순서
'''

# N개의 좌표
N = int(input())
arr = [0] * N
# 좌표를 배정
for i in range(N):
    coordinate = list(map(int, input().split()))
    arr[i] = coordinate

# x 좌표에 대해 우선순위로 정렬하고, 같은 경우 y 좌표에 대해 정렬
arr.sort(key=lambda x: (x[0], x[1]))

# 좌표를 하나씩 출력
for j in arr:
    print(*j)