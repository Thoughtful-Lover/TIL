import sys


# S를 빈 데큐로 설정
S = set()
# 시행횟수 M을 입력 받음
M = int(sys.stdin.readline())
# M번 만큼 시행
for _ in range(M):
    # 명령을 입력 받고
    command = list(sys.stdin.readline().split())
    # 각 문제의 조건에 따라 구현
    # 'add'이면
    if command[0] == 'add':
        # 값을 추가
        S.add(command[1])
    # 'remove'이면
    elif command[0] == 'remove':
        # 값을 제거
        S.discard(command[1])
    # 'check'이면
    elif command[0] == 'check':
        # S에 해당 값이 있을 때, 1을, 없을 때 0을 출력
        if command[1] in S:
            print(1)
        else:
            print(0)
    # 'toggle'이면
    elif command[0] == 'toggle':
        # S에 해당 값이 있으면 제거하고 없으면 추가
        if command[1] in S:
            S.remove(command[1])
        else:
            S.add(command[1])
    # 'all'이면
    elif command[0] == 'all':
        # S를 [1,2,3,...,20]으로
        # 이때 위 코드에서는 str만 쓰기로 했기 때문에 str(i) 처리해주기
        S = set([str(i) for i in range(1, 21)])
    # 'empty'인 경우 빈 배열로 만들어주기
    else:
        S = set()