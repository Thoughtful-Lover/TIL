'''
창용마을에 사는 N명의 사람
1~N번까지 번호가 붙어 있는 사람

두 사람이 서로 알거나 몇 사람 거쳐서 알 수 있는 관계라면
하나의 무리

몇 개의 무리가 있는지?
'''


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    adjl = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        line = list(map(int,input().split()))
        adjl[line[0]].append(line[1])

    for j in range(1, N+1):

