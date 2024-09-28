import heapq as hq
import sys

N, K = map(int, sys.stdin.readline().split())
players = [[] for _ in range(N)]
for _ in range(N):
    P, W = map(int, sys.stdin.readline().split())
    hq.heappush(players[P-1], W)
for _ in range(K):
    for i in range(N):
        if players[i] and players[i][-1] >= 1:
            players[i][-1] -= 1
            hq.heapify(players[i])
value_sum = 0
for j in range(N):
    if players[j]:
        value_sum += players[j][-1]
print(value_sum)