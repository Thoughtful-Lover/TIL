'''
14502. 연구소

N*M 크기의 연구소
빈 칸 = 0, 벽 = 1, 바이러스 = 2
벽이 없으면 바이러스는 퍼져감
벽은 3개 세울 수 있음
바이러스가 퍼질 수 없는 안전 영역의 최대값
'''


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]


