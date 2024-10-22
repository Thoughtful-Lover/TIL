import heapq as hq


q = []
N = int(input())
for _ in range(N):
    x = int(input())
    if not x:
        if q:
            print(-hq.heappop(q))
        else:
            print(0)
    else:
        hq.heappush(q, -x)