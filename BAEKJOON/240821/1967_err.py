n = int(input())
weights = [0]*(n+1)
# 루트 노드의 초기값 세팅. 방향, 깊이, 가중치
weights[0] = (1, 0, 0)
weights[1] = (1, 1, 0)
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    if child == 2:
        weights[2] = (2, 2, weight)
    elif child == 3:
        weights[3] = (3, 2, weight)
    else:
        weights[child] = (weights[parent][0], weights[parent][1]+1, weights[parent][1]+weight)
print(weights)
max_left = [0, 0]
max_right = [0, 0]
for node_info in weights:
    if node_info[0] == 2 and max_left[0] <= node_info[1] and max_left[1] < node_info[2]:
        max_left[0], max_left[1] = node_info[1], node_info[2]
    elif node_info[0] == 3 and max_right[0] <= node_info[1] and max_right[1] < node_info[2]:
        max_right[0], max_right[1] = node_info[1], node_info[2]
print(max_left[1]+max_right[1])