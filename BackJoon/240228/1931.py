'''
1931. 회의실 배정

한 개의 회의실
N개의 회의

최대 사용할 수 있는 회의의 최대 개수
'''


'''# 1차시도_RecursionError
# 회의실에서 회의를 최대한 얼마나 할 수 있는지를 세는 함수 how_many_meeting 를 정의
def how_many_meetings(n):
    global cnt
    # 함수가 호출될 때마다 cnt 를 1 증가
    cnt += 1

    # 종료한 회의 다음으로 회의를 순회하며 시작시간이 종료시간보다 같거나 늦으면 해당 회의로 넘어감
    # 이때 종료한 회의 다음 시작 시간 중 가장 종료 시간이 빠른 회의를 선택하게 됨
    for i in range(n+1, N):
        if meeting_list[i][0] >= meeting_list[n][1]:
            how_many_meetings(i)
            break


N = int(input())
meeting_list = [0] * N
cnt = 0

# 회의와 시작시간과 종료시간 정보를 튜플 형태로 meeting_list 에 저장하고
for j in range(N):
    (s, t) = (map(int, input().split()))
    meeting_list[j] = (s, t)

# 종료 시간이 빠른 순으로 정렬
meeting_list.sort(key=lambda x: x[1])

# 초기 값으로 회의 종료 시간이 가장 빠른 회의를 시작
how_many_meetings(0)

print(cnt)'''


'''# 2차시도_틀렸습니다.
# 내 생각에는 시작시간과 종료 시간이 똑같은 회의의 경우 c = n 일 때, break 가 걸려 틀린 것 같다. 문제 조건을 자세히 읽자
# 회의실에서 회의를 최대한 얼마나 할 수 있는지를 세는 함수 how_many_meeting 를 정의
def how_many_meetings(n):
    global cnt
    # 함수가 호출될 때마다 cnt 를 1 증가
    cnt += 1

    # 종료한 회의 다음으로 회의를 순회하며 시작시간이 종료시간보다 같거나 늦으면 해당 회의로 넘어감
    # 이때 종료한 회의 다음 시작 시간 중 가장 종료 시간이 빠른 회의를 선택하게 됨
    while True:
        # 비교를 위한 c 변수에 n 을 저장
        c = n
        for i in range(n+1, N):
            if meeting_list[i][0] >= meeting_list[n][1]:
                cnt += 1
                n = i
                break
        # 만약 위의 for 문을 종료했는데도 여전히 n 값이 갱신되지 않았다면 while 문을 종료
        if c == n:
            break


N = int(input())
meeting_list = [0] * N
cnt = 0

# 회의와 시작시간과 종료시간 정보를 튜플 형태로 meeting_list 에 저장하고
for j in range(N):
    (s, t) = (map(int, input().split()))
    meeting_list[j] = (s, t)

# 종료 시간이 빠른 순으로 정렬
meeting_list.sort(key=lambda x: x[1])

# 초기 값으로 회의 종료 시간이 가장 빠른 회의를 시작
how_many_meetings(0)

print(cnt)'''


# 회의실에서 회의를 최대한 얼마나 할 수 있는지를 세는 함수 how_many_meeting 를 정의
def how_many_meetings(n):
    global cnt
    # cnt 를 1 증가
    cnt += 1

    # 전체 회의를 순회하며 종료한 회의의 종료시간보다 시작시간이 늦으면 해당 회의를 선택함
    # 이때 종료한 회의 다음 시작 시간 중 가장 종료 시간이 빠른 회의를 선택하게 됨
    for i in range(1, N):
        if meeting_list[i][0] >= meeting_list[n][1]:
            cnt += 1
            n = i


N = int(input())
meeting_list = [0] * N
cnt = 0

# 회의와 시작시간과 종료시간 정보를 튜플 형태로 meeting_list 에 저장하고
for j in range(N):
    (s, t) = (map(int, input().split()))
    meeting_list[j] = (s, t)

# 종료 시간이 빠른 순으로 정렬
meeting_list.sort(key=lambda x: x[1])

# 초기 값으로 회의 종료 시간이 가장 빠른 회의를 시작
how_many_meetings(0)

print(cnt)