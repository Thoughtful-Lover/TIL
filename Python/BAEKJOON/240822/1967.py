# 이제 진짜 구현만 하면 되잖아 한 번 해보자
# 리프 노드 (1번 노드)를 출발점으로 해서 가중치가 가장 높은 곳을 찾고
# 거기를 출발점으로 해서 가중치가 가장 높은 곳을 찾아보자.

# Recursion Limit을 풀어준다.
import sys

sys.setrecursionlimit(10**6)


# 한 노드에서 가장 가중치가 가장 큰 경로를 찾아주는데 사용하는 함수 finding_best_weight_from_node
def finding_best_weight_from_node(current_node, current_weight_sum):
    # global 변수로 one_node랑 one_node_weight를 호출
    global one_node, one_node_weight

    # 해당 노드에서 갈 수 있는 노드를 탐색해서
    for next_node in tree[current_node]:
        # 이미 방문한 곳이라면 continue
        if visited[next_node[0]]:
            continue
        # 아직 방문 안한 곳이라면, 방문 표시하고
        visited[next_node[0]] = 1
        # 가중치를 더해주고 해당 노드로 이동
        finding_best_weight_from_node(next_node[0], current_weight_sum+next_node[1])
        # 함수 호출이 종료된 후 방문 표시를 초기화
        visited[next_node[0]] = 0

    # 위의 반복이 모두 종료되었을 때, 만약 가중치가 더 높은 값을 찾았다면, one_node와 one_node_weight를 초기화
    if one_node_weight < current_weight_sum:
        one_node = current_node
        one_node_weight = current_weight_sum
    return


# 노드의 개수 n을 입력 받고
n = int(input())
# 노드 간의 간선 정보와 가중치를 저장해줄 배열 tree
tree = [[] for _ in range(n+1)]
# 방문 표시를 해줄 배열 visited
visited = [0]*(n+1)
# 특정 노드에서 이동할 수 있는 간선 정보와 해당 간선의 가중치를 모두 노드의 인덱스를 기준으로 append
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# 목표 노드인 one_node와 one_node_weight의 값을 초기
one_node, one_node_weight = 0, 0
# 1번 노드에서 제일 가중치가 높은 노드를 찾기 위한 여정을 시작
# 시작 노드인 1에 방문 표시를 해주고
visited[1] = 1
# 함수를 호출
finding_best_weight_from_node(1, 0)
# 호출이 종료되면 방문 표시를 초기화
visited[1] = 0

# another_node에 기존에 찾았던 리프 노드에서 가장 먼 노드 번호를 입력
another_node = one_node
# 똑같이 목표 노드와 가중치 정보를 초기화 해주고
one_node, one_node_weight = 0, 0
# 시작 노드인 another_node를 방문 표시
visited[another_node] = 1
# 함수 호출
finding_best_weight_from_node(another_node, 0)
# 저장된 가중치 정보를 출력
print(one_node_weight)