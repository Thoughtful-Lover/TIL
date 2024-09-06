import sys
sys.setrecursionlimit(10**4)

# 부모노드를 기준으로 자식 노드들을 탐색해서 가중치가 높은 2개 라인을 더하면 되는거지
def calculate_total_weight(top_node):
    # 부모 노드를 기준으로 자식 노드들까지 쭉 이어진 가중치의 최대 값들을 저장할 배열 weight_total
    weigth_total = []
    # 각 1차 자식 노드들의 값들을 모두 저장할 배열 section_weight
    section_weight = []

    # 부모 노드의 1차 자식 노드들을 검사할 함수
    def child_check(current_node, current_weights_sum):
        # 만약 노드의 끝에 도달하면 현재까지의 가중치 합을 section_weight에 append 한 후 return
        if not tree[current_node]:
            section_weight.append(current_weights_sum)
            return

        # 끝이 아니라면, 가중치 값을 갱신하고 다음 값으로 넘어감
        for next_node in tree[current_node]:
            child_check(next_node[0], current_weights_sum+next_node[1])

    # 만약 top_node로 선정한 node가 자식 노드가 없는 노드면 return
    if not tree[top_node]:
        return

    # top_node 기준으로 1차 자식 노드들을 전부 탐색할거임
    for node in tree[top_node]:
        # 함수를 호출하고
        child_check(node[0], node[1])
        # section_weight 배열에 저장된 값 중 최고로 높은 값만 weight_total 배열에 넣어주고
        weigth_total.append(max(section_weight))
        # section_weight 배열을 초기화
        section_weight.clear()

    # 1차 자식 노드들의 탐색이 끝나면, 내림차순으로 weight_total을 정렬해주고
    weigth_total.sort(reverse=True)
    # 경우를 나눠서 적절한 값을 반환
    if len(weigth_total) >= 2:
        return weigth_total[0]+weigth_total[1]
    elif not weigth_total:
        return 0
    else:
        return weigth_total[0]


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
weights = [0]*(n+1)
for i in range(1, n+1):
    # 위의 함수에서 반환 받은 값들을 weights의 인덱스 번호에 맞춰서 저장하고
    weights[i] = calculate_total_weight(i)
# 그 가중치들 중 가장 큰 값을 반환
print(max(weights))
