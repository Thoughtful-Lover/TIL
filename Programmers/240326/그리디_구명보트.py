'''
구명보트는 한 번에 최대 2명 무게 제한
구명 보트를 최소한으로 쓰면서 사람을 구하는 함수

무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
'''


from collections import deque


def solution(people, limit):
    # 오름차순으로 정리해서
    people.sort()
    # 데크로 만듬
    people = deque(people)
    # 필요한 구명보트를 셀 변수 cnt
    cnt = 0
    # 사람이 남아 있는 동안
    while people:
        # 가장 무거운 사람을 하나 뽑고
        person = people.pop()
        # 만약 아직 남은 사람이 있고 제일 체중 작은 사람을 태워도 limit을 넘지 않는다면
        if people and person+people[0] <= limit:
            people.popleft()
        cnt += 1
    return cnt

'''
그런데 이거는 무조건 체중이 제일 작은 사람을 뽑았는데
원래 그리디라면 태울 수 있는 사람 중에 가장 체중이 높은 사람을 뽑아야 하지 않을까?
'''