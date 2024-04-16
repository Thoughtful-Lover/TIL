'''
8958. OX퀴즈

O는 맞은 문제 X는 틀린 문제
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오
'''


# OX 퀴즈의 결과를 바탕으로 점수를 계산하는 함수 ox_quiz를 정의
def ox_quiz(results):
    # 점수를 저장할 변수 score
    score = 0

    # 입력 받은 ox 퀴즈의 결과 리스트를 순회하며
    for i in range(len(results)):
        # 만약 O라면
        if results[i] == 'O':
            # 처음으로 나온 O는 무조건 1점이고 리스트에도 1점을 저장
            if i == 0:
                score += 1
                results[i] = 1
            # 그게 아니라면 바로 앞의 값에서 1을 추가한 값을 점수로 계산하고 리스트에도 저장
            else:
                score += results[i-1]+1
                results[i] = results[i-1]+1

        # 만약 X가 나온 경우라면 리스트에 0점을 저장
        # 이렇게 하면 O가 연속된 경우 1점씩 추가해서 점수가 저장되고
        # 바로 앞이 X인 경우에는 1점부터 다시 시작하게 됨
        else:
            results[i] = 0

    return score


T = int(input())
for _ in range(T):
    # 'O'와 'X'의 배열을 리스트로 입력 받음
    quiz_result = list(input())
    # 이 리스트를 함수 ox_quiz에 입력하여 반환값을 변수 score_sum에 저장
    score_sum = ox_quiz(quiz_result)
    # score_sum 을 출력
    print(score_sum)