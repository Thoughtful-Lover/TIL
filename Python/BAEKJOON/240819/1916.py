# heapq를 써보자
import heapq as hq


# 다익스트라 알고리즘 시작
def dijkstra(start, end):
    # 빈 배열을 만들고
    queue = []
    # 출발지의 비용과 위치를 heappush
    hq.heappush(queue, (the_way[start], start))
    while queue:
        # 가장 낮은 비용을 우선 하나 뽑아서
        current_cost, current_destination = hq.heappop(queue)
        # 만약 현재 위치까지의 비용이 뽑은 비용보다 낮으면 추가로 값을 갱신할 필요가 없음
        if the_way[current_destination] < current_cost:
            continue

        # 만약 현재 뽑은 값이 현재까지 저장된 비용보다 낮다면, 이 값을 기준으로 다음 node까지의 값을 갱신해 볼 수 있음
        for new_destination, new_cost in routes[current_destination]:
            # 현재 위치까지의 비용과 다음 위치까지의 비용을 더해 section_cost를 계산하고
            section_cost = current_cost + new_cost
            # 만약 갱신한 값이 기존의 비용보다 낮으면
            if section_cost < the_way[new_destination]:
                # 값을 갱신하고
                the_way[new_destination] = section_cost
                # 해당 위치와 위치까지의 비용 정보를 heapq에 다시 넣음. 최소 비용을 기준으로 계속 계산을 하고
                hq.heappush(queue, (section_cost, new_destination))
    # 해당 계산을 마치면 도착지에 저장된 최소 비용 정보를 반환
    return the_way[end]

# 정류장의 총 개수 N과 버스 노선의 개수 M
N = int(input())
M = int(input())
# 버스 운행 정보를 담을 routes
routes = [[] for _ in range(N+1)]
for _ in range(M):
    # 노선의 시작점, 도착점, 비용을 입력 받고
    sp, ep, cost = map(int, input().split())
    # 출발점에 해당하는 인덱스에 입력
    routes[sp].append((ep, cost))
# 그리고 최소비용을 저장할 배열 the_way
the_way = [float('inf')]*(N+1)

# 최소비용을 계산할 출발지와 도착지를 입력받고
departure, arrival = map(int, input().split())
the_way[departure] = 0
# 출발지에서 출발하여 다익스트라 알고리즘 실행
print(dijkstra(departure, arrival))