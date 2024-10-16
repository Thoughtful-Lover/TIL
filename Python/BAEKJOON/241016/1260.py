import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)


def dfs(current_node):
    visited[current_node] = True
    print(current_node, end=' ')
    for node in nodes[current_node]:
        if not visited[node]:
            dfs(node)


def bfs(start_node):
    q = deque()
    q.append(start_node)
    while q:
        current_node = q.popleft()
        visited[current_node] = True
        print(current_node, end=' ')
        for node in nodes[current_node]:
            if not visited[node] and node not in q:
                q.append(node)


# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    if a in nodes[b]:
        continue
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1, N + 1):
    nodes[i].sort()

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)