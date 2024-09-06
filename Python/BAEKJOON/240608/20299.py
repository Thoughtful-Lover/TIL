from collections import deque

N, K, L = map(int, input().split())
team = deque()
for _ in range(N):
    a, b, c = map(int, input().split())
    if a+b+c >= K and a >= L and b >= L and c >= L:
        team.append(a)
        team.append(b)
        team.append(c)
print(len(team)//3)
print(*team)