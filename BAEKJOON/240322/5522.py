'''
5522. 카드 게임

카드 게임은 5회의 게임
그 총점으로 승부
각 게임의 득점을 나타내는 정수가 주어졌을 때, 총점을 구하는 프로그램
'''

# 점수의 총점을 저장할 변수 score_sum
score_sum = 0
# 5회 게임할 동안의 점수를 입력 받고 score_sum에 더해줌
for _ in range(5):
    score = int(input)
    score_sum += score

# score_sum을 출력해줌
print(score_sum)