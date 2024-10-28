from collections import deque

q = deque(input())
sticks = 0
cnt = 0
current = ''
previous = ''
while q:
    previous = current
    current = q.popleft()
    if current == ')' and previous == '(':
        cnt += sticks
    elif current == ')' and previous == ')':
        sticks -= 1
    elif current == '(' and previous == '(':
        sticks += 1
        cnt += 1
print(cnt)