def calculate_total_weight(top_node):
    section_weigth_total = [0] * len(tree[top_node])

    def child_check(current_node):
        # 이 부분에서 bfs를 통해서 최선의 조합을 찾으면 된다!! 좀만 더 파이팅 하자

        while tree[current_node]:
            if len(tree[node]) == 1:
                weights[top_node] += tree[node][0][1]
                node = tree[node][0][0]
            else:
                if (tree[node][0][1] or 0) > (tree[node][1][1] or 0):
                    weights[top_node] += tree[node][0][1]
                    node = tree[node][0][0]
                else:
                    weights[top_node] += (tree[node][1][1] or 0)
                    node = (tree[node][1][0] or 0)

    if not tree[top_node]:
        return

    for node in tree[top_node]:
        weights[top_node] += node[1]
        child_check(node)

    section_weigth_total.sort(reverse=True)
    return max(section_weigth_total[0]+section_weigth_total[1])



n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
weights = [0]*(n+1)
for i in range(1, n+1):
    weights[i] = calculate_total_weight(i)
print(max(weights))
