'''
1260. DFS와 BFS
그래프를 DFS와 BFS로 탐색한 결과를 출력
'''

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
