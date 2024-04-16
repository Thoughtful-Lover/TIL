'''
11723. 집합
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

check 연산이 주어질 때마다, 결과를 출력
'''


# 집합 연산을 수행하는 함수 operation
def operation(es, command):
    # add 이면 집합에 x를 추가
    if command[0] == 'add':
        es.add(int(command[1]))
    # remove 이면 집합에 x를 제거
    elif command[0] == 'remove':
        if command[1] in es:
            es.remove(int(command[1]))
    # check 이면 집합에 x 가 있으면 1을, 없으면 0을 출력
    elif command[0] == 'check':
        if int(command[1]) in es: print(1)
        else: print(0)
    # toggle 이면 집합에 x가 있으면 x를 제거하고, 없으면 x를 추가
    elif command[0] == 'toggle':
        if int(command[1]) in es:
            es.remove(int(command[1]))
        else:
            es.add(int(command[1]))
    # all 이면 1~20까지가 있는 집합으로 바꿈
    elif command[0] == 'all':
        es = {i for i in range(1, 21)}
    # empty 이면 공집합으로 만듬
    elif command[0] == 'empty':
        es = set()

    return es


# 연산의 수 M과 비어 있는 공집합 S
M = int(input())
S = set()
# 연산을 입력 받고 연산을 수행한 결과를 S에 다시 저장
for _ in range(M):
    set_op = list(input().split())
    S = operation(S, set_op)