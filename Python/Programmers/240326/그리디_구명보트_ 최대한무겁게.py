def solution(people, limit):
    people.sort()
    cnt = 0
    while people:
        person = people.pop()
        if people:
            index = -1
            for i in range(len(people)):
                if people[-(i+1)] + person <= limit:
                    index = i
                    break
            if index != -1:
                people.pop(index)
        cnt += 1
    return cnt

# print(solution([70, 50, 80, 50], 100))