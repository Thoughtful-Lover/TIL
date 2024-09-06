'''
13458. 시험감독

총 N개의 시험장, 각각의 시험장마다 응시자들
총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명,
부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명,
각각의 시험장에 총감독관은 오직 1명 부감독관은 여러 명
각 시험장마다 응시생들을 모두 감시해야할 때, 필요한 감독관 수의 최솟값

첫째 줄, 시험장의 개수 N
둘째 줄, 각 시험장에 있는 응시자의 수
셋째 줄에는 B와 C
'''


# 시험장에 필요한 감독관의 최솟값을 계산하는 함수 proctor
# 매개변수인 chief와 vice는 각각 총감독관과 부감독관이 감시할 수 있는 인원의 수
def proctor(chief, vice):
    # 글로벌 변수 cnt를 호출
    global cnt

    # classroom의 학생수들을 순회하며
    for students in classroom:
        # 일단 총감독관은 한 명이 있다고 생각할 때
        cnt += 1
        # 반 학생수가 총감독관 한 명이 감당할 수 있는 인원이면 해당 반은 멈추고 다음 반으로 탐색을 진행
        if students <= chief:
            continue
        # 그게 아니라면 다른 조건들을 확인해보자
        elif students > chief:
            # 먼저 총감독관 한 명 분의 인원수를 빼고
            students -= chief
            # 남은 학생수를 부감독관이 감당 가능한 학생의 수로 나눈 몫을 부감독관의 수로 cnt에 더해줌
            cnt += students//vice
            # 이 때, 0보다 크고 vice보다 작은 수가 남을 경우 부감독관을 추가로 1명 더 배정해줌
            if students%vice > 0:
                cnt +=1


# 총 반의 개수 N, 각 반별 학생 수를 classroom 이라는 리스트에 저장
# B와 C는 총감독관과 부감독관 각각이 감시할 수 있는 학생의 수
N = int(input())
classroom = list(map(int, input().split()))
B, C = map(int, input().split())
# 필요한 감독관의 수를 저장할 변수 cnt
cnt = 0
proctor(B, C)
print(cnt)