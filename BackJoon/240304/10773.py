'''
10773. 제로

숫자를 하나씩 입력 받는데
0을 외치면 가장 최근에 넣은 수를 지움
'''

N = int(input())
# 빈 스택을 하나 정의
stack = []
# N개의 수를 입력 받아 0이면 최근에 들어간 수를 빼주고, 아니면 stack 에 저장해준다.
for i in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

# stack 내의 수들을 더해줌
print(sum(stack))