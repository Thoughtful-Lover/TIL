'''
29725. 체스 초보 브실이

체스판의 기물 점수는 백의 기물 점수 합에서 흑의 기물 접수 합을 뺀 값
킹, 폰, 나이트, 비숍, 룩, 퀸의 기물 점수는 각각 0, 1, 3, 3, 5, 9

대문자는 백, 소문자는 흑

.: 빈칸
K 또는 k: 킹
P 또는 p: 폰
N 또는 n: 나이트
B 또는 b: 비숍
R 또는 r: 룩
Q 또는 q: 퀸
'''

# 기물 점수의 초기값을 정의
score = 0

# 체스판이 총 8줄이더라
for _ in range(8):
    # 리스트에 개별 문자로 받고
    row = list(input())
    # 걱 라수투룰 순회하며 백이면 점수를 더해주고 흑이면 빼줌
    for square in row:
        if square == 'P':
            score += 1
        elif square == 'p':
            score -= 1
        elif square == 'N':
            score += 3
        elif square == 'n':
            score -= 3
        elif square == 'B':
            score += 3
        elif square == 'b':
            score -= 3
        elif square == 'R':
            score += 5
        elif square == 'r':
            score -= 5
        elif square == 'Q':
            score += 9
        elif square == 'q':
            score -= 9
# 최종 점수를 출력
print(score)