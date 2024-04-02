'''
14888. 연산자 끼워 넣기
'''


def calculation(time, sub_sum, total):
    global max_num
    global min_num

    # if sub_sum > min_num and sub_sum < max_num:
    #     return

    if time == total:
        if max_num < sub_sum:
            max_num = sub_sum
        if min_num > sub_sum:
            min_num = sub_sum

    for i in range(4):
        if operator[i]:
            if i == 0:
                new_sum = sub_sum + numbers[time]
                operator[i] -= 1
                calculation(time+1, new_sum, total)
                operator[i] += 1
            elif i == 1:
                new_sum = sub_sum - numbers[time]
                operator[i] -= 1
                calculation(time+1, new_sum, total)
                operator[i] += 1
            elif i == 2:
                new_sum = sub_sum * numbers[time]
                operator[i] -= 1
                calculation(time+1, new_sum, total)
                operator[i] += 1
            else:
                if sub_sum < 0:
                    new_sum = -(-sub_sum//numbers[time])
                else:
                    new_sum = sub_sum // numbers[time]
                operator[i] -= 1
                calculation(time+1, new_sum, total)
                operator[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

calculation(1, numbers[0], N)
print(max_num)
print(min_num)