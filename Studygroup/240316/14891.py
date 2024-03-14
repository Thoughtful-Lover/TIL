'''
14891. 톱니바퀴

총 8개의 톱니를 가진 톱니바퀴 4개
톱니는 N극 또는 S극
왼쪽부터 1~4번 톱니바퀴

톱니바퀴를 총 K번 회전
톱니바퀴의 회전은 한 칸을 기준
회전은 시계 방향 또는 반시계 방향

회전 방향에 따라 회전
회전하기 전 맞닿은 부분의 극이 다르면 옆에는 회전한 방향과 반대방향으로 회전

최종 상태를 구하는 프로그램

첫째줄부터 넷째줄까지 톱니바퀴의 상태
12시방향부터 시계방향 순서대로
N극은 0, S극은 1

다섯째줄 회전 횟수 K
다음 K개의 정수 묶음
첫 번째 정수는 회전시킬 톱니바퀴 번호, 두 번째 정수는 방향
1은 시계, -1은 반시계

1, 2, 3, 4 번 톱니바퀴의 12시 방향이 N극이면 0점,
S극이면 각각 1, 2, 4, 8 점
'''

from collections import deque


def rotate(number, direction):
    if direction == 1:
        gear[number].appendleft(gear[number].pop())

        if number+1 <= 3 and adj[number][1] != adj[number+1][0]:
            rotate(number+1, -direction)
        if number-1 >= 0 and adj[number][0] != adj[number-1][1]:
            rotate(number-1, -direction)

    else:
        gear[number].append(gear[number].popleft())

        if number+1 <= 3 and adj[number][1] != adj[number+1][0]:
            rotate(number+1, -direction)
        if number-1 >= 0 and adj[number][0] != adj[number-1][1]:
            rotate(number-1, -direction)


def score():
    score = 0
    for i in range(4):
        if gear[i][0] == '1':
            score += 2 ** i
    return score


gear = deque(deque(input()) for _ in range(4))
print(gear)

K = int(input())
for _ in range(K):
    n, d = map(int, input().split())

    adj = deque()
    for i in range(4):
        adj_sub = deque()
        adj_sub.append(gear[i][6])
        adj_sub.append(gear[i][2])
        adj.append(adj_sub)

    rotate_check = [0] * 4

    rotate(n-1, d)

print(score())