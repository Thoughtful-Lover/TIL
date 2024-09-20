'''
1189. 컴백홈

한수는 집에 간다.
한수는 왼쪽 아래점 집은 오른쪽 위
한수는 한 번 지나친 곳을 다시 방문하지 않는다.

T로 표시된 부분 가지 못함
R*C 맵에 못가는 부분이 주어지고 거리 K가 주어지면
한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수

R (1<=R<=5)
C (1<=C<=5)
K (1<=K<=R*C)

두 번째부터 R+1번째 줄까지는 R*C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열
'''

R, C, K = map(int, input().split())
roads = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
si, sj = R-1, 0
cnt = 0
visited[si][sj] = 1
