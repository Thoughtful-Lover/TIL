import heapq as hq

T = int(input())
for _ in range(T):
    K = int(input())
    chapters = list(map(int, input().split()))
    chapters.sort()
    cnt = 0
    while len(chapters) > 1:
      a = hq.heappop(chapters)
      b = hq.heappop(chapters)
      cnt += (a+b)
      hq.heappush(chapters, a+b)
    print(cnt)