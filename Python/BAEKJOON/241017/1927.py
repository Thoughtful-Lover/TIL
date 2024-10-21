import heapq as hq

array = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not array:
            print(0)
        else:
            print(hq.heappop(array))
    else:
        hq.heappush(array, x)