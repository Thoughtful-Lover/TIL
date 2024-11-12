# 참가자 수 입력
N = int(input())
# attendants 배열을 2차원으로 만들어서, 점수의 총합, 제출 횟수, 마지막으로 점수를 획득한 문제의 업로드 시간을 각각 평가혀록 함
attendants = [[] for _ in range(3)]
# 각 참가자의 정보를 각각의 배열에 입력
for _ in range(N):
    a, b, c = map(int, input().split())
    attendants[0].append(a)
    attendants[1].append(b)
    attendants[2].append(c)
x = ''
# 반복문
while True:
    # 점수 총합의 최대값이 하나이면
    if attendants[0].count(max(attendants[0])) == 1:
        # 그 값을 가진 사람이 우승자
        print(attendants[0].index(max(attendants[0])) + 1)
        break
    # 그게 아니면서 만약에 점수 최소값을 가진 사람이 1명이면
    elif attendants[0].count(min(attendants[0])) == 1:
        # 해당 사람을 따로 저장해서 이후 계산에서 배제
        x = attendants[0].index(min(attendants[0]))
        attendants[1][x] = float('inf')
        attendants[2][x] = float('inf')
    # 제출 횟수가 적은 사람이 1명이면
    elif attendants[1].count(min(attendants[1])) == 1:
        # 해당 사람을 출력
        print(attendants[1].index(min(attendants[1])) + 1)
        break

    # 만약 위의 경우에도 걸리지 않는다면, 문제 업로드 시간까지 계산
    else:
        print(attendants[2].index(min(attendants[2])) + 1)
        break