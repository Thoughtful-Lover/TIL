'''
10039. 평균 점수

5명의 점수가 주어졌을 때 평균 점수
40점 미만인 점수는 보충수업을 필수적으로 들어 40점으로 적용
'''

# 학생들의 전체 점수를 저장할 변수 score_sum
score_sum = 0
# 학생 5명의 점수를 입력 받되
for _ in range(5):
    # 각 학생이 받은 점수를 입력 받고
    score = int(input())
    # 40점 미만이면 40점을 더해주고
    if score < 40:
        score_sum += 40
    # 나머지 경우에는 획득한 점수를 더해줌
    else:
        score_sum += score
# 평균을 구해서 출력
print(score_sum//5)