# heapq를 써보자
import heapq as hq


# 다익스트라 알고리즘 시작
def dijkstra(boarding, previous):
    global arrival

    # 현재 위치에서 갈수 있는 위치 중 비용이 적은 것부터 계산해본다.
    while routes[boarding]:
        # 현재 위치에서 가장 적은 비용이 드는 노선을 하나 뽑는다.
        current_cost, current_departure = hq.heappop(routes[boarding])
        # 만약 해당 노선의 비용 + 해당 노선의 출발지까지의 기존 비용이 도착 노선까지 드는 기존 비용보다 적으면 값을 갱신
        if the_way[current_departure] > current_cost+previous:
            the_way[current_departure] = current_cost+previous
        # 그게 아니라면 다른 값들을 갱신
        else:
            continue
        # 만약 도착지에 도착했다면 더이상 탐색할 필요가 없으므로 continue
        if current_departure == arrival:
            continue
        # 다음 탐색으로 넘어감
        dijkstra(current_departure, the_way[current_departure])


# 정류장의 총 개수 N과 버스 노선의 개수 M
N = int(input())
M = int(input())
# 버스 운행 정보를 담을 routes
routes = [[] for _ in range(N+1)]
for _ in range(M):
    # 노선의 시작점, 도착점, 비용을 입력 받고
    sp, ep, cost = map(int, input().split())
    # 출발점에 해당하는 인덱스에 비용이 낮은 순으로 정리되도록 입력
    hq.heappush(routes[sp], (cost, ep))
# 그리고 최소비용을 저장할 배열 the_way
the_way = [100000*N]*(N+1)

# 최소비용을 계산할 출발지와 도착지를 입력받고
departure, arrival = map(int, input().split())
the_way[departure] = 0
# 출발지에서 출발하여 다익스트라 알고리즘 실행
dijkstra(departure, 0)
print(the_way[arrival])