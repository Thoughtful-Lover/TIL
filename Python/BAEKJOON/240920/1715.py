import heapq as hq

N = int(input())
cards = []
cnt = 0
for i in range(N):
    hq.heappush(cards, int(input()))
while len(cards) > 1:
    A = hq.heappop(cards)
    B = hq.heappop(cards)
    cnt += A+B
    hq.heappush(cards, A+B)
print(cnt)