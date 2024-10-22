import sys

sys.setrecursionlimit(10 * 6)


def dfs(current_position, current_time):
    global t, K

    if t <= current_time:
        return
    elif current_position == K:
        if t > current_time:
            t = current_time
        return

    if current_position == 0:
        return
    else:
        dfs(current_position + 1, current_time + 1)
        dfs(current_position - 1, current_time + 1)
        dfs(current_position * 2, current_time + 1)


N, K = map(int, input().split())
t = 10 ** 5
dfs(N, 0)
print(t)