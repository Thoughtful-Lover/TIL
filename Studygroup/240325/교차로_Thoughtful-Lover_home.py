import sys
from collections import deque

def traffic_police():
    road_first = [-1]*4
    while road[0] or road[1] or road[2] or road[3]:
        for i in range(4):
            if road[i]:
                road_first[i] = road[i].popleft()


N = int(sys.stdin.readline())
pass_time = [-1] * N
road = [deque() for _ in range(4)]
for _ in range(N):
    time, position = sys.stdin.readline().split()
    time = int(time)
    road[ord(position)-65].append(time)
