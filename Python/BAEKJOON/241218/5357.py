from collections import deque

N = int(input())
for _ in range(N):
    stack = []
    data = deque(input())
    while data:
        datum = data.popleft()
        if not stack or stack[-1] != datum:
            stack.append(datum)
    for letter in stack:
        print(letter, end='')
    print()