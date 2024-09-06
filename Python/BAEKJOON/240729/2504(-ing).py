'''
2504. 괄호의 값

괄호가 모두 짝이 맞게 맞추어져야 올바른 괄호열
올바르지 않은 괄호열이면 0을 출력

1. '()'인 괄호열의 값은 2
2. '[]'인 괄호열의 값은 3이다.
3. '(X)'의 괄호값은 2x값(X)으로 계산
4. '[X]'의 괄호값은 3x값(X)으로 계산
5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY) = 값(X) + 값(Y)로 계산
'''


from collections import deque

brackets_q = deque(input())
q = deque()
num = deque()
top = -1
while brackets_q:
    bracket = brackets_q.popleft()
    if q:
        if q[top] == '(' and bracket == ')':
            if num:
                num[-1] *= 2
            else:
                num.append(2)
            q.pop()
            top -= 1
        elif q[top] == '[' and bracket == ']':
            if num:
                num[-1] *= 3
            else:
                num.append(3)
            q.pop()
            top -= 1
    else:
        num.append(0)
        q.append(bracket)
        top += 1
print(sum(num))
