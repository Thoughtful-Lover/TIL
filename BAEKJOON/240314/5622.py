'''
5622. 다이얼

1번까지 전화 거는데 걸리는 시간 2초
그 다음부터 +1 할 때마다 1초씩 더걸림
2~8까지 알파벳 대문자 3개씩
9에는 알파벳 대문자 4개

문자열을 입력 받았을 때 해당 다이얼을 돌리는데 걸리는 최소 시간
'''


# 다이얼을 돌리는데 걸리는 시간을 계산하는 함수 dial을 정의
def dial(string_list):
    # 총 걸리는 시간을 저장할 변수 time_sum 을 정의
    time_sum = 0
    # 입력 받은 리스트를 순회하며
    for alph in string_list:

        # 단어가 3개씩 적혀 있으므로
        time = ord(alph) - 62

        if time//3 < 7:
            # 3개씩 묶어서 걸리는 시간을 더해주되 1번 다이얼까지는 2초가 걸리므로 2초씩 추가해준다.
            time_sum += (time//3) + 2

        # 7번 숫자에는 알파벳이 4개 적혀 있어서 해당 조건에 맞게 조건을 주었다.
        elif 6 <= time/3 <= 7:
            time_sum += 8

        # 8번 숫자에 해당하는 경우에 맞게 조건을 주었다.
        elif 7 < time/3 <= 8:
            time_sum += 9

        # 9번 숫자는 나머지 경우로 나눠주었다.
        else:
            time_sum += 10

    return time_sum


# 걸어야할 전화번호의 단어를 리스트로 입력 받음
arr = list(input())
print(dial(arr))